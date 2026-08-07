"""
Database and service client factories.

Qdrant:  local file mode by default (no Docker).
         Set QDRANT_URL in .env to switch to cloud.
Redis:   Upstash or any Redis-compatible URL via REDIS_URL.
"""

import os
from functools import lru_cache

import redis.asyncio as aioredis
from qdrant_client import AsyncQdrantClient

from app.config import get_settings


@lru_cache
def get_qdrant_client() -> AsyncQdrantClient:
    """
    Return a cached Qdrant client.

    - QDRANT_URL is set  → connect to cloud / self-hosted server
    - QDRANT_URL is empty → local file mode (qdrant_data/, no Docker)
    """
    settings = get_settings()
    url = settings.qdrant_url.strip()

    if url:
        return AsyncQdrantClient(
            url=url,
            api_key=settings.qdrant_api_key or None,
        )

    # Local file mode — data persists in QDRANT_LOCAL_PATH
    path = settings.qdrant_local_path
    os.makedirs(path, exist_ok=True)
    return AsyncQdrantClient(path=path)


@lru_cache
def get_redis_client() -> aioredis.Redis:
    """
    Return a cached async Redis client.

    Uses REDIS_URL from .env (Upstash rediss:// or local redis://).
    """
    settings = get_settings()
    return aioredis.from_url(
        settings.redis_url,
        encoding="utf-8",
        decode_responses=True,
    )
