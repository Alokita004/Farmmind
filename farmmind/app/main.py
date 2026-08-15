from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from farmmind.app.api.routes.chat import router as chat_router
from farmmind.app.api.routes.farm import router as farm_router
from farmmind.app.api.routes.health import router as health_router
from farmmind.app.api.routes.knowledge import router as knowledge_router

app = FastAPI(
    title="FarmMind MVP",
    description="Multi-agent AI platform for agricultural decision support.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(chat_router)
app.include_router(farm_router)
app.include_router(knowledge_router)


@app.get("/", tags=["root"])
async def root() -> dict:
    return {"message": "FarmMind API is running"}
