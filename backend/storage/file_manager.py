import json
from pathlib import Path

from config import STORAGE_DIR
from logger.setup import get_logger

log = get_logger("storage")


def _ensure_dir() -> None:
    STORAGE_DIR.mkdir(parents=True, exist_ok=True)


def get_file_path(filename: str) -> Path:
    _ensure_dir()
    return STORAGE_DIR / filename


def save_text(filename: str, content: str) -> Path:
    path = get_file_path(filename)
    path.write_text(content, encoding="utf-8")
    log.info("Saved text file: %s", path)
    return path


def load_text(filename: str) -> str | None:
    path = get_file_path(filename)
    if not path.exists():
        log.warning("Text file not found: %s", path)
        return None
    return path.read_text(encoding="utf-8")


def append_jsonl(filename: str, data: dict) -> None:
    path = get_file_path(filename)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(data, ensure_ascii=False) + "\n")


def load_jsonl(filename: str) -> list[dict]:
    path = get_file_path(filename)
    if not path.exists():
        return []
    items: list[dict] = []
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                items.append(json.loads(line))
    return items


def save_json(filename: str, data: dict) -> Path:
    path = get_file_path(filename)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    log.info("Saved JSON file: %s", path)
    return path


def load_json(filename: str) -> dict | None:
    path = get_file_path(filename)
    if not path.exists():
        log.warning("JSON file not found: %s", path)
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def clear_storage() -> None:
    _ensure_dir()
    for item in STORAGE_DIR.iterdir():
        if item.is_file():
            item.unlink()
            log.debug("Deleted: %s", item)
    log.info("Storage cleared")
