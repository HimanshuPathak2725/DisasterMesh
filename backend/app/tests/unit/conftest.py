"""
conftest.py for unit tests.

Provides an in-memory SQLite database for ingest endpoint tests so they do
not require a real on-disk database or a running server lifespan.
"""

from __future__ import annotations

import pytest
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.models import Base

# ── In-memory async SQLite engine (shared across all unit tests) ──────────────

_TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope="session")
async def test_engine():
    """Create all tables in an in-memory SQLite DB once per test session."""
    engine = create_async_engine(_TEST_DATABASE_URL, echo=False, future=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield engine
    await engine.dispose()


@pytest.fixture()
async def db_session(test_engine):
    """Yield a fresh async session, rolling back after each test."""
    session_factory = async_sessionmaker(
        bind=test_engine,
        expire_on_commit=False,
        class_=AsyncSession,
    )
    async with session_factory() as session:
        yield session
        await session.rollback()


@pytest.fixture(autouse=True)
def patch_get_db(db_session, monkeypatch):
    """
    Replace the FastAPI `get_db` dependency with one that returns the
    test session.  `autouse=True` applies to all tests in this package
    so ingest endpoint tests always use the in-memory DB.
    """
    async def _override():
        yield db_session

    # Patch the dependency on the router module
    import app.routers.ingest as ingest_mod
    monkeypatch.setattr(ingest_mod, "get_db", _override)

    # Also patch the app's dependency overrides
    from app.db import get_db
    from app.main import app
    app.dependency_overrides[get_db] = _override
    yield
    app.dependency_overrides.pop(get_db, None)


@pytest.fixture(autouse=True)
def patch_init_db(monkeypatch):
    """Prevent lifespan from calling the real init_db (we handle DB setup above)."""
    import app.main as main_mod

    async def _noop():
        pass

    monkeypatch.setattr(main_mod, "init_db", _noop)
