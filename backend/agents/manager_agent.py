from __future__ import annotations

import json
import re

from logger.setup import get_logger
from models.model_router import call_model, get_next_model, handle_model_error
from storage.file_manager import save_text
from streaming.sse_manager import send_event

log = get_logger("manager_agent")

SYSTEM_PROMPT = """You are a senior dataset quality manager. You review expanded dataset \
prompts and decide whether they are detailed enough to produce a high-quality fine-tuning \
dataset.

Respond ONLY with valid JSON (no markdown, no extra text):
{
  "decision": "APPROVE" | "REJECT",
  "confidence": <float 0-1>,
  "feedback": "<constructive feedback or empty string if approved>"
}

Evaluate these criteria:
- Clear persona definition
- Sufficient domain detail
- Diversity / edge-case coverage
- Formatting and style guidance
- Consistency with any provided memory facts"""

MAX_REJECTION_CYCLES = 3


async def review_prompt(expanded_prompt: str) -> tuple[bool, str, float]:
    """Ask the manager model to review an expanded prompt.

    Returns ``(approved, feedback_or_prompt, confidence)``.
    """
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"Review this expanded prompt:\n\n{expanded_prompt}"},
    ]

    model = get_next_model(preferred="moonshotai/kimi-k2-instruct")
    if model is None:
        raise RuntimeError("No available model for manager review")

    try:
        raw = await call_model(model, messages, temperature=0.3, max_tokens=1024)
    except Exception as exc:
        log.warning("Model %s failed: %s — switching", model, exc)
        await send_event("model_switch", {"from": model, "reason": str(exc)})
        model = handle_model_error(model, exc)
        if model is None:
            raise RuntimeError("All models exhausted during manager review") from exc
        raw = await call_model(model, messages, temperature=0.3, max_tokens=1024)

    # Parse the JSON response (strip markdown fences if present)
    cleaned = re.sub(r"```json\s*|\s*```", "", raw).strip()
    try:
        result = json.loads(cleaned)
    except json.JSONDecodeError:
        log.error("Manager returned invalid JSON: %s", raw[:200])
        return True, expanded_prompt, 0.5  # fallback: auto-approve

    approved = result.get("decision", "APPROVE").upper() == "APPROVE"
    feedback = result.get("feedback", "")
    confidence = float(result.get("confidence", 0.5))
    return approved, feedback, confidence


async def approval_loop(
    expanded_prompt: str,
    user_prompt: str,
    memory_facts: list[str] | None = None,
) -> str:
    """Run the manager review loop (max 3 rejections, then auto-approve)."""
    await send_event("stage_update", {"stage": 2, "status": "running", "label": "Manager review"})

    current_prompt = expanded_prompt

    for cycle in range(1, MAX_REJECTION_CYCLES + 1):
        log.info("Manager review cycle %d", cycle)
        approved, feedback, confidence = await review_prompt(current_prompt)

        await send_event(
            "log",
            {
                "stage": 2,
                "cycle": cycle,
                "approved": approved,
                "confidence": confidence,
                "feedback": feedback[:200],
            },
        )

        if approved:
            log.info("Prompt approved (confidence=%.2f)", confidence)
            break

        if cycle == MAX_REJECTION_CYCLES:
            log.warning("Max rejections reached — auto-approving on cycle %d", cycle)
            break

        log.info("Prompt rejected — refining with feedback")
        # Re-expand with feedback
        from agents.prompt_expander import expand_prompt

        current_prompt = await expand_prompt(
            f"{user_prompt}\n\nPrevious feedback to address:\n{feedback}",
            memory_facts,
        )

    save_text("stage2_approved_prompt.txt", current_prompt)
    await send_event("stage_update", {"stage": 2, "status": "complete", "label": "Prompt approved"})
    return current_prompt
