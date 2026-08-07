"""
DisasterMesh FastAPI application entrypoint.

Run locally:
    cd backend
    uvicorn app.main:app --reload --port 8000
"""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.db import init_db
from app.routers import dispatch, health, incidents, ingest

settings = get_settings()

logging.basicConfig(
    level=settings.log_level.upper(),
    format="%(asctime)s [%(levelname)s] %(name)s — %(message)s",
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("DisasterMesh API starting — env=%s", settings.app_env)
    await init_db()
    logger.info("Database tables initialised")
    yield
    logger.info("DisasterMesh API shutting down")



# ── App ───────────────────────────────────────────────────────────────────────

app = FastAPI(
    title="DisasterMesh API",
    description=(
        "Multi-agent disaster response coordination system. "
        "Fuses satellite, social, citizen, and IoT signals into "
        "verified, prioritized, and dispatched incidents."
    ),
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# ── CORS (Next.js frontend at localhost:3000) ─────────────────────────────────

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://*.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Routers ───────────────────────────────────────────────────────────────────

app.include_router(health.router)
app.include_router(ingest.router, prefix="/ingest", tags=["Ingestion"])
app.include_router(incidents.router, prefix="/incidents", tags=["Incidents"])
app.include_router(dispatch.router, prefix="/dispatch", tags=["Dispatch"])
