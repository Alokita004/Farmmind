from __future__ import annotations

import uuid

from fastapi import APIRouter

from farmmind.app.graph.workflow import build_workflow
from farmmind.app.schemas.requests import ChatRequest
from farmmind.app.schemas.responses import ChatResponse

router = APIRouter(prefix="/api/v1", tags=["chat"])


@router.post("/chat", response_model=ChatResponse, summary="Run a farm advisory chat workflow")
async def chat(request: ChatRequest) -> ChatResponse:
    workflow = build_workflow()
    state = {
        "user_query": request.query,
        "farmer_profile": request.farmer.model_dump(),
        "crop_data": request.crop.model_dump(),
        "required_agents": [],
        "final_response": "",
    }

    result = workflow.invoke(state)
    analysis = {
        "crop_health": result.get("crop_health_result", {}),
        "advisory": result.get("advisory_result", {}),
        "market": result.get("market_result", {}),
        "profit": result.get("profit_result", {}),
        "sustainability": result.get("sustainability_result", {}),
    }
    recommendation = result.get("recommendation_result", {})
    return ChatResponse(
        request_id=str(uuid.uuid4()),
        query=request.query,
        agents_used=result.get("required_agents", []),
        analysis=analysis,
        recommendation=recommendation,
        final_answer=result.get("final_response", "Recommendation generated.")
    )
