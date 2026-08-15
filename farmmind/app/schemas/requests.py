from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field, field_validator


class FarmerProfile(BaseModel):
    name: str = Field(..., min_length=1)
    location: str = Field(..., min_length=1)
    farm_size_acres: float = Field(..., gt=0)


class CropData(BaseModel):
    name: str = Field(..., min_length=1)
    expected_yield_quintals: float = Field(..., gt=0)


class ChatRequest(BaseModel):
    query: str = Field(..., min_length=3)
    farmer: FarmerProfile
    crop: CropData

    @field_validator("query")
    @classmethod
    def validate_query(cls, value: str) -> str:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("query cannot be blank")
        return cleaned


class KnowledgeIngestRequest(BaseModel):
    text: str = Field(..., min_length=10)
    metadata: dict | None = None


class AgentRoutingResult(BaseModel):
    intents: list[str] = Field(default_factory=list)

    @field_validator("intents")
    @classmethod
    def validate_intents(cls, value: list[str]) -> list[str]:
        valid = {
            "crop_health",
            "advisory",
            "market",
            "profit",
            "sustainability",
            "complete_analysis",
        }
        cleaned = []
        for item in value:
            if item in valid:
                cleaned.append(item)
        return cleaned


class AnalysisRequest(BaseModel):
    query: str = Field(..., min_length=3)
    farmer: FarmerProfile
    crop: CropData
