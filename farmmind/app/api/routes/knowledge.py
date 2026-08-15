from __future__ import annotations

from fastapi import APIRouter

from farmmind.app.schemas.requests import KnowledgeIngestRequest
from farmmind.app.tools.knowledge_tools import build_knowledge_base, search_agricultural_knowledge

router = APIRouter(prefix="/api/v1", tags=["knowledge"])


@router.post("/knowledge/ingest", summary="Ingest small knowledge base for agricultural advice")
async def ingest_knowledge(payload: KnowledgeIngestRequest):
    try:
        build_knowledge_base()
        return {"status": "ok", "message": "Knowledge base ingested successfully."}
    except Exception as exc:  # pragma: no cover
        return {"status": "error", "message": str(exc)}


@router.post("/knowledge/search", summary="Search agricultural knowledge base")
async def search_knowledge(query: str):
    return {"results": search_agricultural_knowledge(query)}
