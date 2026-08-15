from __future__ import annotations

from sqlalchemy.orm import Session

from farmmind.app.db.models import Crop, Farm, Farmer, FarmAnalysis, Recommendation


class FarmerRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_farmer(self, name: str, location: str) -> Farmer:
        obj = Farmer(name=name, location=location)
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj


class FarmRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_farm(self, farmer_id: int, name: str, farm_size_acres: float, location: str) -> Farm:
        obj = Farm(farmer_id=farmer_id, name=name, farm_size_acres=farm_size_acres, location=location)
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj


class CropRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_crop(self, farm_id: int, name: str, expected_yield_quintals: float) -> Crop:
        obj = Crop(farm_id=farm_id, name=name, expected_yield_quintals=expected_yield_quintals)
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj


class AnalysisRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_analysis(self, farmer_id: int, farm_id: int, crop_id: int, query: str, analysis_json: dict) -> FarmAnalysis:
        obj = FarmAnalysis(
            farmer_id=farmer_id,
            farm_id=farm_id,
            crop_id=crop_id,
            query=query,
            analysis_json=str(analysis_json),
        )
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj


class RecommendationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_recommendation(self, farm_id: int, crop_name: str, overall_score: float, risk_level: str, recommendation_text: str) -> Recommendation:
        obj = Recommendation(
            farm_id=farm_id,
            crop_name=crop_name,
            overall_score=overall_score,
            risk_level=risk_level,
            recommendation_text=recommendation_text,
        )
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj
