from fastapi import FastAPI
from app.api.routes.health import router as health_router


app = FastAPI(
    title="InsureMind AI",
    description="Agentic Enterprise Knowledge Intelligence Platform",
    version="0.1.0"
)

app.include_router(health_router)