from __future__ import annotations

import asyncio
import json
import re

from config import DEDUP_THRESHOLD
from dedup.embedder import get_embedding
from dedup.faiss_store import FaissStore
from logger.setup import get_logger
from models.model_router import call_model, get_next_model, handle_model_error
from storage.file_manager import append_jsonl
from streaming.sse_manager import send_event

log = get_logger("dataset_generator")

SYSTEM_PROMPT = """You are a dataset sample generator. Given a scenario and a dataset \
description, produce question-answer pairs in ShareGPT format.

Return ONLY a JSON array of objects. Each object must follow this exact schema:
{
  "conversations": [
    {"from": "human", "value": "<user question>"},
    {"from": "gpt", "value": "<assistant answer>"}
  ]
}

Rules:
- Questions must be realistic and varied
- Answers must be detailed, helpful, and accurate
- Do NOT add any commentary outside the JSON array
- Ensure diversity across samples"""

MEMORY_INJECTION_INTERVAL = 20
MAX_DUP_RETRIES = 3


async def generate_samples_for_scenario(
    scenario: str,
    approved_prompt: str,
    memory_facts: list[str] | None,
    num_samples: int,
    scenario_index: int,
    faiss_store: FaissStore,
) -> list[dict]:
    """Generate *num_samples* QA pairs for a single scenario."""
    await send_event(
        "progress",
        {"stage": 4, "scenario_index": scenario_index, "scenario": scenario, "target": num_samples, "completed": 0},
    )

    all_samples: list[dict] = []
    generated = 0
    batch_size = min(num_samples, 5)  # request a handful at a time

    while generated < num_samples:
        remaining = num_samples - generated
        current_batch = min(batch_size, remaining)

        # Build prompt with optional memory injection
        memory_block = ""
        if memory_facts and generated % MEMORY_INJECTION_INTERVAL < batch_size:
            memory_block = "\n\nMemory facts (incorporate naturally):\n" + "\n".join(
                f"- {fact}" for fact in memory_facts
            )

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": (
                    f"Dataset description:\n{approved_prompt}\n\n"
                    f"Scenario: {scenario}{memory_block}\n\n"
                    f"Generate exactly {current_batch} diverse QA pair(s)."
                ),
            },
        ]

        model = get_next_model()
        if model is None:
            log.error("No available model — stopping scenario %d", scenario_index)
            break

        for _attempt in range(3):
            try:
                raw = await call_model(model, messages, temperature=0.85, max_tokens=4096)
                break
            except Exception as exc:
                log.warning("Model %s error: %s — rotating", model, exc)
                await send_event("model_switch", {"from": model, "reason": str(exc)})
                model = handle_model_error(model, exc)
                if model is None:
                    break
        else:
            break  # all retries exhausted

        if model is None:
            break

        # Parse JSON array from response
        samples = _parse_samples(raw)
        if not samples:
            log.warning("No valid samples parsed for scenario %d — retrying", scenario_index)
            continue

        # Dedup each sample
        for sample in samples:
            if generated >= num_samples:
                break

            sample_text = _sample_to_text(sample)
            dup_passed = False

            for retry in range(MAX_DUP_RETRIES + 1):
                try:
                    emb = await get_embedding(sample_text)
                    is_dup, score = faiss_store.is_duplicate(emb)
                    if not is_dup:
                        faiss_store.add(emb)
                        dup_passed = True
                        break
                    log.debug(
                        "Duplicate (score=%.3f) on retry %d for scenario %d",
                        score, retry, scenario_index,
                    )
                except Exception as emb_exc:
                    log.warning("Embedding/dedup error: %s — skipping dedup", emb_exc)
                    dup_passed = True
                    break

            if dup_passed:
                all_samples.append(sample)
                append_jsonl("dataset_final.jsonl", sample)
                generated += 1

        await send_event(
            "progress",
            {
                "stage": 4,
                "scenario_index": scenario_index,
                "scenario": scenario,
                "target": num_samples,
                "completed": generated,
            },
        )

    log.info("Scenario %d (%s): generated %d/%d samples", scenario_index, scenario, generated, num_samples)
    return all_samples


async def run_all_generators(
    scenarios: list[str],
    approved_prompt: str,
    memory_facts: list[str] | None,
    target_size: int,
) -> list[dict]:
    """Distribute sample targets across scenarios and run concurrently."""
    await send_event("stage_update", {"stage": 4, "status": "running", "label": "Generating dataset"})

    faiss_store = FaissStore(dimension=1024, threshold=DEDUP_THRESHOLD)

    num_scenarios = len(scenarios)
    base_per_scenario = target_size // num_scenarios
    remainder = target_size % num_scenarios

    tasks = []
    for idx, scenario in enumerate(scenarios):
        count = base_per_scenario + (1 if idx < remainder else 0)
        if count == 0:
            continue
        tasks.append(
            generate_samples_for_scenario(
                scenario=scenario,
                approved_prompt=approved_prompt,
                memory_facts=memory_facts,
                num_samples=count,
                scenario_index=idx,
                faiss_store=faiss_store,
            )
        )

    results = await asyncio.gather(*tasks, return_exceptions=True)

    all_samples: list[dict] = []
    for res in results:
        if isinstance(res, Exception):
            log.error("Generator task failed: %s", res)
            continue
        all_samples.extend(res)

    await send_event(
        "stage_update",
        {"stage": 4, "status": "complete", "label": f"{len(all_samples)} samples generated"},
    )
    log.info("Stage 4 complete — total samples: %d", len(all_samples))
    return all_samples


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _parse_samples(raw: str) -> list[dict]:
    """Best-effort parse of a JSON array of ShareGPT samples."""
    # Strip markdown code fences if present
    cleaned = re.sub(r"```json\s*|\s*```", "", raw).strip()
    try:
        data = json.loads(cleaned)
    except json.JSONDecodeError:
        # Try to find JSON array in the text
        match = re.search(r"\[.*\]", cleaned, re.DOTALL)
        if match:
            try:
                data = json.loads(match.group())
            except json.JSONDecodeError:
                return []
        else:
            return []

    if isinstance(data, dict):
        data = [data]
    if not isinstance(data, list):
        return []

    valid: list[dict] = []
    for item in data:
        if isinstance(item, dict) and "conversations" in item:
            valid.append(item)
    return valid


def _sample_to_text(sample: dict) -> str:
    """Flatten a ShareGPT sample to plain text for embedding."""
    parts: list[str] = []
    for turn in sample.get("conversations", []):
        parts.append(f"{turn.get('from', '')}: {turn.get('value', '')}")
    return "\n".join(parts)
