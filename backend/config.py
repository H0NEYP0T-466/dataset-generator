import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# ---------------------------------------------------------------------------
# API Keys
# ---------------------------------------------------------------------------
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
LONGCAT_API_KEY = os.getenv("LONGCAT_API_KEY", "")
CEREBRAS_API_KEY = os.getenv("CEREBRAS_API_KEY", "")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY", "")

# ---------------------------------------------------------------------------
# Provider base URLs
# ---------------------------------------------------------------------------
GROQ_BASE = "https://api.groq.com/openai/v1"
LONGCAT_BASE = "https://api.longcat.cloud/openai/v1"
CEREBRAS_BASE = "https://api.cerebras.ai/v1"
MISTRAL_BASE = "https://api.mistral.ai/v1"

# ---------------------------------------------------------------------------
# Model configurations
# Each entry maps a model name to its provider details and rate limits.
# ---------------------------------------------------------------------------
MODEL_CONFIGS: dict[str, dict] = {
    # Groq models
    "moonshotai/kimi-k2-instruct": {
        "provider": "groq",
        "base_url": GROQ_BASE,
        "api_key_env": "GROQ_API_KEY",
        "daily_limit": 1_000,
        "monthly_limit": 30_000,
    },
    "llama-3.1-8b-instant": {
        "provider": "groq",
        "base_url": GROQ_BASE,
        "api_key_env": "GROQ_API_KEY",
        "daily_limit": 14_400,
        "monthly_limit": 500_000,
    },
    "llama-4-scout-17b-16e-instruct": {
        "provider": "groq",
        "base_url": GROQ_BASE,
        "api_key_env": "GROQ_API_KEY",
        "daily_limit": 14_400,
        "monthly_limit": 500_000,
    },
    "llama-3.3-70b-versatile": {
        "provider": "groq",
        "base_url": GROQ_BASE,
        "api_key_env": "GROQ_API_KEY",
        "daily_limit": 14_400,
        "monthly_limit": 500_000,
    },
    "qwen/qwen3-32b": {
        "provider": "groq",
        "base_url": GROQ_BASE,
        "api_key_env": "GROQ_API_KEY",
        "daily_limit": 14_400,
        "monthly_limit": 500_000,
    },
    # LongCat models
    "LongCat-Flash-Lite": {
        "provider": "longcat",
        "base_url": LONGCAT_BASE,
        "api_key_env": "LONGCAT_API_KEY",
        "daily_limit": 50_000,
        "monthly_limit": 1_000_000,
    },
    "LongCat-Flash-Chat": {
        "provider": "longcat",
        "base_url": LONGCAT_BASE,
        "api_key_env": "LONGCAT_API_KEY",
        "daily_limit": 50_000,
        "monthly_limit": 1_000_000,
    },
    "LongCat-Flash-Thinking": {
        "provider": "longcat",
        "base_url": LONGCAT_BASE,
        "api_key_env": "LONGCAT_API_KEY",
        "daily_limit": 50_000,
        "monthly_limit": 1_000_000,
    },
    "LongCat-Flash-Thinking-2601": {
        "provider": "longcat",
        "base_url": LONGCAT_BASE,
        "api_key_env": "LONGCAT_API_KEY",
        "daily_limit": 50_000,
        "monthly_limit": 1_000_000,
    },
    # Cerebras models
    "gpt-oss-120b": {
        "provider": "cerebras",
        "base_url": CEREBRAS_BASE,
        "api_key_env": "CEREBRAS_API_KEY",
        "daily_limit": 14_400,
        "monthly_limit": 500_000,
    },
    "llama3.1-8b": {
        "provider": "cerebras",
        "base_url": CEREBRAS_BASE,
        "api_key_env": "CEREBRAS_API_KEY",
        "daily_limit": 14_400,
        "monthly_limit": 500_000,
    },
    # Mistral models
    "mistral-large-2411": {
        "provider": "mistral",
        "base_url": MISTRAL_BASE,
        "api_key_env": "MISTRAL_API_KEY",
        "daily_limit": 14_400,
        "monthly_limit": 500_000,
    },
    "mistral-small-2503": {
        "provider": "mistral",
        "base_url": MISTRAL_BASE,
        "api_key_env": "MISTRAL_API_KEY",
        "daily_limit": 14_400,
        "monthly_limit": 500_000,
    },
    "open-mixtral-8x22b": {
        "provider": "mistral",
        "base_url": MISTRAL_BASE,
        "api_key_env": "MISTRAL_API_KEY",
        "daily_limit": 14_400,
        "monthly_limit": 500_000,
    },
    "mistral-embed": {
        "provider": "mistral",
        "base_url": MISTRAL_BASE,
        "api_key_env": "MISTRAL_API_KEY",
        "daily_limit": 14_400,
        "monthly_limit": 500_000,
    },
}

# ---------------------------------------------------------------------------
# Model priority for auto-switching (first = preferred)
# ---------------------------------------------------------------------------
MODEL_PRIORITY: list[str] = [
    "moonshotai/kimi-k2-instruct",
    "llama-3.3-70b-versatile",
    "qwen/qwen3-32b",
    "llama-4-scout-17b-16e-instruct",
    "mistral-large-2411",
    "gpt-oss-120b",
    "LongCat-Flash-Thinking-2601",
    "LongCat-Flash-Thinking",
    "LongCat-Flash-Chat",
    "mistral-small-2503",
    "open-mixtral-8x22b",
    "llama-3.1-8b-instant",
    "llama3.1-8b",
    "LongCat-Flash-Lite",
]

# ---------------------------------------------------------------------------
# Deduplication
# ---------------------------------------------------------------------------
DEDUP_THRESHOLD: float = float(os.getenv("DEDUP_THRESHOLD", "0.85"))

# ---------------------------------------------------------------------------
# Dataset generation limits
# ---------------------------------------------------------------------------
MAX_DATASET_SIZE: int = int(os.getenv("MAX_DATASET_SIZE", "200000"))

# ---------------------------------------------------------------------------
# Storage
# ---------------------------------------------------------------------------
STORAGE_DIR: Path = Path(__file__).resolve().parent / "storage"
STORAGE_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Helper to resolve an API key at runtime
# ---------------------------------------------------------------------------
_KEY_MAP = {
    "GROQ_API_KEY": GROQ_API_KEY,
    "LONGCAT_API_KEY": LONGCAT_API_KEY,
    "CEREBRAS_API_KEY": CEREBRAS_API_KEY,
    "MISTRAL_API_KEY": MISTRAL_API_KEY,
}


def get_api_key(env_name: str) -> str:
    return _KEY_MAP.get(env_name, "")
