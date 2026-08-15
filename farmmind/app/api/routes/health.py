from fastapi import APIRouter

from farmmind.app.schemas.responses import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse, summary="Health check")
def health_check() -> HealthResponse:
    return HealthResponse(status="healthy")
