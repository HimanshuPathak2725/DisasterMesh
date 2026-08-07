"""
Database and service client factories.

Qdrant:      local file mode by default (no Docker).
             Set QDRANT_URL in .env to switch to cloud.
Redis:       Upstash or any Redis-compatible URL via REDIS_URL.
SQLAlchemy:  async SQLite via aiosqlite.  Switch DATABASE_URL to
             postgresql+asyncpg:// for production.
"""

from __future__ import annotations

import os
from collections.abc import AsyncGenerator
from functools import lru_cache

import redis.asyncio as aioredis
from qdrant_client import AsyncQdrantClient
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.config import get_settings


# ── Qdrant ────────────────────────────────────────────────────────────────────


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


# ── Redis ─────────────────────────────────────────────────────────────────────


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


# ── SQLAlchemy (async SQLite / Postgres) ──────────────────────────────────────

_engine = None
_session_factory: async_sessionmaker[AsyncSession] | None = None


def _get_engine():
    global _engine
    if _engine is None:
        settings = get_settings()
        _engine = create_async_engine(
            settings.database_url,
            echo=False,
            future=True,
        )
    return _engine


def _get_session_factory() -> async_sessionmaker[AsyncSession]:
    global _session_factory
    if _session_factory is None:
        _session_factory = async_sessionmaker(
            bind=_get_engine(),
            expire_on_commit=False,
            class_=AsyncSession,
        )
    return _session_factory


async def init_db() -> None:
    """
    Create all ORM tables on startup (idempotent).

    Called once from the FastAPI lifespan context manager.
    """
    from app.models import Base  # local import avoids circular deps at module level

    async with _get_engine().begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    FastAPI dependency — yields an async DB session per request.

    Usage in a router:
        async def my_route(db: AsyncSession = Depends(get_db)):
            ...
    """
    async with _get_session_factory()() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
