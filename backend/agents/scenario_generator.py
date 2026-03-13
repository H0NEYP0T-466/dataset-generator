from __future__ import annotations

from logger.setup import get_logger
from models.model_router import call_model, get_next_model, handle_model_error
from storage.file_manager import save_text
from streaming.sse_manager import send_event


log = get_logger("scenario_generator")

SYSTEM_PROMPT = """You are a scenario-planning specialist for fine-tuning datasets.

Given an approved dataset prompt, generate a numbered list of diverse scenario headings \
that fully cover the topic. Each scenario should represent a distinct sub-topic, edge \
case, difficulty level, or user-intent variation. You are a middle agent in a dataset \
generation pipeline, and your output will be used to create specific question-answer \
pairs for LLM fine-tuning.

The requested dataset size controls scenario breadth:
- Small target sizes should use fewer, high-signal scenarios
- Large target sizes should use more scenarios for better coverage and variety
- Ensure the scenario set can realistically support the requested number of samples

If relevant, include greeting/opening scenarios and then expand to a wide range of
intents, contexts, and edge cases.
Rules:
- Generate exactly the number of scenarios requested by the user message
- Each scenario is a SHORT heading (one line)
- Cover easy, medium, and hard difficulty
- Include common AND edge-case situations
- Return ONLY the numbered list, nothing else

Example format:
1. Basic greeting and introduction
2. Handling ambiguous user queries
3. Multi-turn follow-up conversations
..."""


def _target_scenario_count(target_dataset_size: int) -> int:
    """Scale scenario count with dataset size while keeping a practical range."""
    # Roughly 6-10 samples per scenario, clamped for quality and latency.
    return max(12, min(60, target_dataset_size // 8))


async def generate_scenarios(approved_prompt: str, target_dataset_size: int = 100) -> list[str]:
    """Stage 3 — produce scenario headings from the approved prompt."""
    await send_event("stage_update", {"stage": 3, "status": "running", "label": "Generating scenarios"})

    scenario_count = _target_scenario_count(target_dataset_size)

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": (
                f"Approved prompt:\n\n{approved_prompt}\n\n"
                f"Target dataset size: {target_dataset_size}\n"
                f"Generate exactly {scenario_count} scenarios."
            ),
        },
    ]

    model = get_next_model(preferred="mistral-large-2411")
    if model is None:
        model = get_next_model(preferred="gpt-oss-120b")
    if model is None:
        raise RuntimeError("No available model for scenario generation")

    try:
        raw = await call_model(model, messages, temperature=0.8, max_tokens=2048)
    except Exception as exc:
        log.warning("Model %s failed: %s — switching", model, exc)
        await send_event("model_switch", {"from": model, "reason": str(exc)})
        model = handle_model_error(model, exc)
        if model is None:
            raise RuntimeError("All models exhausted during scenario generation") from exc
        raw = await call_model(model, messages, temperature=0.8, max_tokens=2048)

    # Parse numbered list
    scenarios: list[str] = []
    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        # Strip leading number/dot/dash
        cleaned = line.lstrip("0123456789.-) ").strip()
        if cleaned:
            scenarios.append(cleaned)

    if len(scenarios) > scenario_count:
        scenarios = scenarios[:scenario_count]

    if not scenarios:
        scenarios = ["General dataset scenario"]

    save_text("stage3_scenarios.txt", "\n".join(scenarios))
    await send_event(
        "stage_update",
        {"stage": 3, "status": "complete", "label": f"{len(scenarios)} scenarios generated"},
    )
    log.info("Stage 3 complete — %d scenarios", len(scenarios))
    return scenarios
