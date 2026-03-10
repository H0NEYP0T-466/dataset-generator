from __future__ import annotations

from pathlib import Path

import faiss
import numpy as np

from logger.setup import get_logger

log = get_logger("faiss_store")


class FaissStore:
    """Manages a FAISS index for cosine-similarity deduplication."""

    def __init__(self, dimension: int = 1024, threshold: float = 0.85) -> None:
        self.dimension = dimension
        self.threshold = threshold
        # IndexFlatIP computes inner product; we normalise vectors so IP == cosine sim
        self.index: faiss.IndexFlatIP = faiss.IndexFlatIP(dimension)
        log.info("FAISS index created (dim=%d, threshold=%.2f)", dimension, threshold)

    def _normalise(self, vec: list[float]) -> np.ndarray:
        arr = np.array(vec, dtype=np.float32).reshape(1, -1)
        norm = np.linalg.norm(arr)
        if norm > 0:
            arr /= norm
        return arr

    def is_duplicate(self, embedding: list[float]) -> tuple[bool, float]:
        """Check whether a similar vector already exists in the index.

        Returns ``(is_dup, similarity_score)``.
        """
        if self.index.ntotal == 0:
            return False, 0.0

        query = self._normalise(embedding)
        distances, _ = self.index.search(query, 1)
        score = float(distances[0][0])
        is_dup = score >= self.threshold
        if is_dup:
            log.debug("Duplicate detected (score=%.4f)", score)
        return is_dup, score

    def add(self, embedding: list[float]) -> None:
        vec = self._normalise(embedding)
        self.index.add(vec)
        log.debug("Vector added — total vectors: %d", self.index.ntotal)

    def reset(self) -> None:
        self.index.reset()
        log.info("FAISS index reset")

    def save(self, path: str | Path) -> None:
        faiss.write_index(self.index, str(path))
        log.info("FAISS index saved to %s", path)

    def load(self, path: str | Path) -> None:
        path = Path(path)
        if path.exists():
            self.index = faiss.read_index(str(path))
            log.info("FAISS index loaded from %s (%d vectors)", path, self.index.ntotal)
        else:
            log.warning("FAISS index file not found: %s", path)
