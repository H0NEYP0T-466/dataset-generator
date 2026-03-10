from __future__ import annotations

from logger.setup import get_logger
from models.model_router import call_model, get_next_model, handle_model_error
from storage.file_manager import save_text
from streaming.sse_manager import send_event

log = get_logger("prompt_expander")

SYSTEM_PROMPT = """You are a dataset-design expert. Your job is to take a short, raw \
user prompt and expand it into a rich, detailed persona and task description that can \
be used to generate a high-quality fine-tuning dataset.

Your expanded prompt MUST include:
1. A clear persona definition (who the AI should act as)
2. The domain / topic scope
3. Desired response style, length, and tone
4. Edge cases and diversity requirements
5. Any constraints or formatting rules

If memory facts are provided, incorporate them naturally to maintain consistency.

Return ONLY the expanded prompt text — no commentary, no markdown headers."""


async def expand_prompt(
    user_prompt: str,
    memory_facts: list[str] | None = None,
) -> str:
    """Stage 1 — expand a raw user prompt into a detailed dataset brief."""
    await send_event("stage_update", {"stage": 1, "status": "running", "label": "Expanding prompt"})

    memory_block = ""
    if memory_facts:
        memory_block = "\n\nMemory facts to incorporate:\n" + "\n".join(
            f"- {fact}" for fact in memory_facts
        )

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": f"Raw prompt:\n{user_prompt}{memory_block}",
        },
    ]

    preferred_model = "LongCat-Flash-Lite"
    model = get_next_model(preferred=preferred_model)
    if model is None:
        raise RuntimeError("No available model for prompt expansion")

    try:
        expanded = await call_model(model, messages, temperature=0.7, max_tokens=8192)
    except Exception as exc:
        log.warning("Model %s failed: %s — switching", model, exc)
        await send_event("model_switch", {"from": model, "reason": str(exc)})
        model = handle_model_error(model, exc)
        if model is None:
            raise RuntimeError("All models exhausted during prompt expansion") from exc
        expanded = await call_model(model, messages, temperature=0.7, max_tokens=8192)

    save_text("stage1_expanded_prompt.txt", expanded)
    await send_event("stage_update", {"stage": 1, "status": "complete", "label": "Prompt expanded"})
    log.info("Stage 1 complete — expanded prompt length: %d", len(expanded))
    return expanded
