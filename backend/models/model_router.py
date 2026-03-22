from __future__ import annotations

import re
import time
from typing import Any

import httpx

from config import MODEL_CONFIGS, MODEL_PRIORITY, get_api_key
from logger.setup import get_logger

log = get_logger("model_router")

# ---------------------------------------------------------------------------
# Shared HTTP client (created lazily, reused across calls)
# ---------------------------------------------------------------------------
_http_client: httpx.AsyncClient | None = None


def _get_client() -> httpx.AsyncClient:
    global _http_client
    if _http_client is None or _http_client.is_closed:
        _http_client = httpx.AsyncClient(timeout=120.0)
    return _http_client

# ---------------------------------------------------------------------------
# In-memory usage tracking
# ---------------------------------------------------------------------------
_model_usage: dict[str, dict[str, int]] = {}
_blacklisted: dict[str, float] = {}  # model -> timestamp when blacklisted

BLACKLIST_TTL = 60.0  # seconds to keep a model blacklisted after rate-limit


def _usage(model: str) -> dict[str, int]:
    if model not in _model_usage:
        _model_usage[model] = {"requests": 0, "tokens": 0}
    return _model_usage[model]


def _parse_limit(raw_limit: Any) -> int | None:
    """Return numeric limit if finite, otherwise None for unlimited/unknown."""
    if isinstance(raw_limit, int):
        return raw_limit
    if isinstance(raw_limit, str):
        lowered = raw_limit.strip().lower()
        if lowered == "unlimited":
            return None
        digits = re.sub(r"[^0-9]", "", lowered)
        if digits:
            return int(digits)
    return None


def _is_available(model: str) -> bool:
    cfg = MODEL_CONFIGS.get(model)
    if cfg is None:
        return False
    if not get_api_key(cfg["api_key_env"]):
        return False
    if model in _blacklisted:
        if time.time() - _blacklisted[model] < BLACKLIST_TTL:
            return False
        del _blacklisted[model]
    usage = _usage(model)
    daily_limit = _parse_limit(cfg.get("daily_limit"))
    if daily_limit is not None and usage["requests"] >= daily_limit:
        return False
    return True


# ---------------------------------------------------------------------------
# Public helpers
# ---------------------------------------------------------------------------

def get_next_model(preferred: str | None = None) -> str | None:
    """Return the next available model, optionally starting with *preferred*."""
    if preferred and _is_available(preferred):
        return preferred
    for model in MODEL_PRIORITY:
        if _is_available(model):
            return model
    log.error("All models exhausted!")
    return None


def handle_model_error(model_name: str, error: Exception) -> str | None:
    """Blacklist *model_name* and return the next available model."""
    log.warning("Blacklisting %s due to error: %s", model_name, error)
    _blacklisted[model_name] = time.time()
    return get_next_model()


async def call_model(
    model_name: str,
    messages: list[dict[str, str]],
    temperature: float = 0.7,
    max_tokens: int = 4096,
) -> str:
    """Call an OpenAI-compatible chat completions endpoint and return the
    assistant message content.  Raises on non-2xx responses.
    """
    cfg = MODEL_CONFIGS.get(model_name)
    if cfg is None:
        raise ValueError(f"Unknown model: {model_name}")

    api_key = get_api_key(cfg["api_key_env"])
    if not api_key:
        raise ValueError(f"Missing API key for {model_name} ({cfg['api_key_env']})")

    url = f"{cfg['base_url']}/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload: dict[str, Any] = {
        "model": model_name,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }

    log.debug("Calling %s  (temp=%.1f, max_tokens=%d)", model_name, temperature, max_tokens)

    client = _get_client()
    resp = await client.post(url, json=payload, headers=headers)

    if resp.status_code == 429:
        raise httpx.HTTPStatusError(
            "Requests per minute limit reached", request=resp.request, response=resp
        )

    resp.raise_for_status()
    data = resp.json()

    usage = _usage(model_name)
    usage["requests"] += 1
    if "usage" in data:
        usage["tokens"] += data["usage"].get("total_tokens", 0)

    content: str = data["choices"][0]["message"]["content"]
    log.info("Response from %s — %d chars", model_name, len(content))
    return content


def get_model_status() -> list[dict[str, Any]]:
    """Return status of every configured model for the dashboard."""
    statuses: list[dict[str, Any]] = []
    for name, cfg in MODEL_CONFIGS.items():
        usage = _usage(name)
        statuses.append(
            {
                "model": name,
                "provider": cfg["provider"],
                "available": _is_available(name),
                "requests_used": usage["requests"],
                "tokens_used": usage["tokens"],
                "daily_limit": cfg["daily_limit"],
                "monthly_limit": cfg["monthly_limit"],
                "blacklisted": name in _blacklisted,
            }
        )
    return statuses


def reset_usage() -> None:
    """Reset all in-memory usage counters (for fresh runs)."""
    _model_usage.clear()
    _blacklisted.clear()
