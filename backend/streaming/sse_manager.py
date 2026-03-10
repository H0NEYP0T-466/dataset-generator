from __future__ import annotations

import asyncio
import json
from typing import AsyncGenerator

from logger.setup import get_logger

log = get_logger("sse")

# Global event queue shared across the application
_event_queue: asyncio.Queue[dict | None] = asyncio.Queue()


async def send_event(event_type: str, data: dict | str) -> None:
    """Push an SSE event onto the global queue."""
    payload = {
        "event": event_type,
        "data": data if isinstance(data, str) else json.dumps(data, ensure_ascii=False),
    }
    await _event_queue.put(payload)
    log.debug("SSE event queued: %s", event_type)


async def event_generator() -> AsyncGenerator[dict, None]:
    """Async generator that yields SSE events from the global queue."""
    while True:
        item = await _event_queue.get()
        if item is None:
            # Sentinel – end of stream
            break
        yield item


async def send_sentinel() -> None:
    """Push a None sentinel to signal the end of the SSE stream."""
    await _event_queue.put(None)


def reset_queue() -> None:
    """Drain the existing event queue for a fresh pipeline run."""
    while not _event_queue.empty():
        try:
            _event_queue.get_nowait()
        except asyncio.QueueEmpty:
            break
    log.debug("SSE event queue drained")
