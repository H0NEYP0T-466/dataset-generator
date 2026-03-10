from __future__ import annotations

from logger.setup import get_logger
from models.model_router import call_model, get_next_model, handle_model_error
from storage.file_manager import save_text
from streaming.sse_manager import send_event

log = get_logger("scenario_generator")

SYSTEM_PROMPT = """You are a scenario-planning specialist for fine-tuning datasets.

Given an approved dataset prompt, generate a numbered list of diverse scenario headings \
that fully cover the topic. Each scenario should represent a distinct sub-topic, edge \
case, difficulty level, or user-intent variation.

Rules:
- Generate between 10 and 30 scenarios
- Each scenario is a SHORT heading (one line)
- Cover easy, medium, and hard difficulty
- Include common AND edge-case situations
- Return ONLY the numbered list, nothing else

Example format:
1. Basic greeting and introduction
2. Handling ambiguous user queries
3. Multi-turn follow-up conversations
..."""


async def generate_scenarios(approved_prompt: str) -> list[str]:
    """Stage 3 — produce scenario headings from the approved prompt."""
    await send_event("stage_update", {"stage": 3, "status": "running", "label": "Generating scenarios"})

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"Approved prompt:\n\n{approved_prompt}"},
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

    if not scenarios:
        scenarios = ["General dataset scenario"]

    save_text("stage3_scenarios.txt", "\n".join(scenarios))
    await send_event(
        "stage_update",
        {"stage": 3, "status": "complete", "label": f"{len(scenarios)} scenarios generated"},
    )
    log.info("Stage 3 complete — %d scenarios", len(scenarios))
    return scenarios
