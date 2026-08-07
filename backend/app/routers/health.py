"""Health check router."""

from fastapi import APIRouter

from app.config import get_settings
from app.schemas import HealthResponse

router = APIRouter(tags=["Health"])


@router.get("/health", response_model=HealthResponse, summary="Health check")
async def health() -> HealthResponse:
    """Returns 200 when the API is up. Used by CI and load balancers."""
    settings = get_settings()
    return HealthResponse(environment=settings.app_env)
