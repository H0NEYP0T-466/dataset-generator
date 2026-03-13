from __future__ import annotations

from logger.setup import get_logger
from models.model_router import call_model, get_next_model, handle_model_error
from storage.file_manager import save_text
from streaming.sse_manager import send_event



log = get_logger("prompt_expander")

SYSTEM_PROMPT = """You are an elite dataset-design architect with deep expertise in \
LLM fine-tuning, persona engineering, and conversational AI. You are the FIRST agent \
in a multi-stage dataset generation pipeline:

  [YOU: Prompt Enhancer] → [Scenario Planner] → [Sample Generator]

Your sole job is to transform a short raw user prompt into a rich, detailed dataset \
specification that the downstream Scenario Planner and Sample Generator agents will \
use to produce high-quality fine-tuning data. You do NOT generate scenarios or \
samples yourself — you only write the specification.

Given a raw prompt, expand it into a dense specification covering ALL of the following:

1. PERSONA DEFINITION
   - Who the AI is (name, archetype, background if relevant)
   - Core personality traits, quirks, and behavioral tendencies
   - How the persona speaks (vocabulary level, formality, mannerisms, catchphrases)
   - What the persona loves, avoids, and reacts strongly to
   - Emotional range and how mood shifts across different contexts

2. DOMAIN & TOPIC SCOPE
   - Primary subject matter and knowledge boundaries
   - Sub-topics that must be covered for the persona to feel complete
   - Topics that are out of scope or require careful handling
   - Real-world context or setting the persona operates in

3. RESPONSE STYLE, LENGTH & TONE
   - Tone spectrum (e.g., warm, clinical, playful, authoritative)
   - Typical response length ranges for different query types
   - Formatting preferences (lists vs prose, use of examples, emojis, etc.)
   - How tone and style shift across emotional or contextual situations

4. CONSISTENCY & MEMORY RULES
   - Hard facts, preferences, or history the persona must always remember
   - How the persona handles contradictions or attempts to break character
   - How the persona responds to out-of-scope or ambiguous queries
   - Relationship dynamic between the persona and the user

5. CONSTRAINTS & HARD RULES
   - Absolute rules the persona never violates under any circumstances
   - Safety, ethical, or content boundaries
   - Output format or structural preferences for generated samples

If memory facts are provided, weave them naturally into the persona definition and \
consistency rules — they are non-negotiable truths that all downstream agents must respect."""


async def expand_prompt(
    user_prompt: str,
    memory_facts: list[str] | None = None,
    sample_count: int | None = None,
) -> str:
    """Stage 1 — expand a raw user prompt into a detailed dataset brief."""
    await send_event("stage_update", {"stage": 1, "status": "running", "label": "Expanding prompt"})

    memory_block = ""
    if memory_facts:
        memory_block = "\n\nMemory facts to incorporate:\n" + "\n".join(
            f"- {fact}" for fact in memory_facts
        )

    dataset_size_block = ""
    if sample_count is not None:
        dataset_size_block = (
            "\n\nTarget dataset size requested by user: "
            f"{sample_count} samples. "
            "Design the specification so downstream stages can create enough diverse "
            "coverage to support this size while preserving quality."
        )

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": f"Raw prompt:\n{user_prompt}{memory_block}{dataset_size_block}",
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
