from __future__ import annotations

import httpx

from config import MISTRAL_API_KEY, MISTRAL_BASE
from logger.setup import get_logger

log = get_logger("embedder")


async def get_embedding(text: str) -> list[float]:
    """Obtain an embedding vector from the Mistral embed endpoint."""
    if not MISTRAL_API_KEY:
        raise ValueError("MISTRAL_API_KEY is not set")

    url = f"{MISTRAL_BASE}/embeddings"
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "mistral-embed",
        "input": [text],
    }

    async with httpx.AsyncClient(timeout=60.0) as client:
        resp = await client.post(url, json=payload, headers=headers)

    resp.raise_for_status()
    data = resp.json()
    embedding: list[float] = data["data"][0]["embedding"]
    log.debug("Embedding obtained — %d dimensions", len(embedding))
    return embedding
