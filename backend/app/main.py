
from fastapi import FastAPI

from app.core.config import get_settings
from app.api.routes.health import router as health_router


settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    description="Agentic Enterprise Knowledge Intelligence Platform",
    version=settings.app_version,
    debug=settings.debug,
)

app.include_router(health_router)
