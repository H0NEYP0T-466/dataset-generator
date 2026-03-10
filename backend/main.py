from __future__ import annotations

import asyncio
import json
import time

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from sse_starlette.sse import EventSourceResponse

from agents.dataset_generator import run_all_generators
from agents.manager_agent import approval_loop
from agents.prompt_expander import expand_prompt
from agents.scenario_generator import generate_scenarios
from config import MAX_DATASET_SIZE
from logger.setup import get_logger
from models.model_router import get_model_status, reset_usage
from storage.file_manager import (
    clear_storage,
    get_file_path,
    load_text,
    save_json,
)
from streaming.sse_manager import event_generator, reset_queue, send_event, send_sentinel

log = get_logger("main")

# ---------------------------------------------------------------------------
# FastAPI application
# ---------------------------------------------------------------------------
app = FastAPI(
    title="DataForge — LLM Fine-Tuning Dataset Generator",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------------------------
# Request / response models
# ---------------------------------------------------------------------------


class GenerateRequest(BaseModel):
    prompt: str = Field(..., min_length=1, description="Raw user prompt")
    memory_facts: list[str] = Field(default_factory=list, description="Memory facts for consistency")
    dataset_size: int = Field(default=100, ge=1, le=MAX_DATASET_SIZE, description="Target dataset size")


class GenerateResponse(BaseModel):
    status: str
    message: str


# ---------------------------------------------------------------------------
# Pipeline state
# ---------------------------------------------------------------------------
_pipeline_running = False


async def _run_pipeline(req: GenerateRequest) -> None:
    """Execute the full dataset generation pipeline (Stages 1-4)."""
    global _pipeline_running
    _pipeline_running = True
    start = time.time()

    try:
        # Stage 1 — Expand prompt
        expanded = await expand_prompt(req.prompt, req.memory_facts or [])

        # Stage 2 — Manager approval loop
        approved = await approval_loop(expanded, req.prompt, req.memory_facts or [])

        # Stage 3 — Scenario generation
        scenarios = await generate_scenarios(approved)

        # Stage 4 — Parallel dataset generation
        samples = await run_all_generators(
            scenarios=scenarios,
            approved_prompt=approved,
            memory_facts=req.memory_facts or [],
            target_size=req.dataset_size,
        )

        elapsed = time.time() - start

        # Save metadata
        metadata = {
            "prompt": req.prompt,
            "memory_facts": req.memory_facts,
            "target_size": req.dataset_size,
            "actual_size": len(samples),
            "scenarios_count": len(scenarios),
            "elapsed_seconds": round(elapsed, 2),
        }
        save_json("metadata.json", metadata)

        await send_event("complete", {
            "total_samples": len(samples),
            "elapsed_seconds": round(elapsed, 2),
        })
        log.info("Pipeline complete — %d samples in %.1fs", len(samples), elapsed)

    except Exception as exc:
        log.error("Pipeline failed: %s", exc, exc_info=True)
        await send_event("error", {"message": str(exc)})
    finally:
        await send_sentinel()
        _pipeline_running = False


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------


@app.post("/api/generate", response_model=GenerateResponse)
async def start_generation(req: GenerateRequest):
    """Kick off the dataset generation pipeline in the background."""
    global _pipeline_running
    if _pipeline_running:
        raise HTTPException(status_code=409, detail="A pipeline is already running")

    # Reset state for a fresh run
    clear_storage()
    reset_queue()
    reset_usage()

    asyncio.create_task(_run_pipeline(req))
    return GenerateResponse(status="started", message="Pipeline started — connect to /api/stream for progress")


@app.get("/api/stream")
async def stream_progress():
    """SSE endpoint for live pipeline progress."""
    return EventSourceResponse(
        _sse_generator(),
        media_type="text/event-stream",
    )


async def _sse_generator():
    """Wrap event_generator into the shape sse-starlette expects."""
    async for evt in event_generator():
        yield {
            "event": evt["event"],
            "data": evt["data"],
        }


@app.get("/api/models/status")
async def models_status():
    """Return current model limits and usage for the dashboard."""
    return get_model_status()


@app.get("/api/download/dataset")
async def download_dataset():
    """Download the final JSONL dataset file."""
    path = get_file_path("dataset_final.jsonl")
    if not path.exists():
        raise HTTPException(status_code=404, detail="Dataset file not found — run a generation first")
    return FileResponse(path, media_type="application/jsonl", filename="dataset_final.jsonl")


@app.get("/api/storage/{filename}")
async def view_storage_file(filename: str):
    """Return the contents of any file in the storage directory."""
    content = load_text(filename)
    if content is None:
        # Try loading as JSON
        path = get_file_path(filename)
        if not path.exists():
            raise HTTPException(status_code=404, detail=f"File not found: {filename}")
        content = path.read_text(encoding="utf-8")

    # Attempt to parse as JSON for nicer response
    try:
        return json.loads(content)
    except (json.JSONDecodeError, TypeError):
        return {"filename": filename, "content": content}


@app.delete("/api/reset")
async def reset_all():
    """Clear storage and reset state."""
    global _pipeline_running
    if _pipeline_running:
        raise HTTPException(status_code=409, detail="Cannot reset while pipeline is running")
    clear_storage()
    reset_queue()
    reset_usage()
    return {"status": "ok", "message": "Storage cleared and state reset"}
