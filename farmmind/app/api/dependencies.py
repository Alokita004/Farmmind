from __future__ import annotations

from typing import Generator

from fastapi import Depends
from sqlalchemy.orm import Session

from farmmind.app.db.database import SessionLocal


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_current_user():
    return {"user": "demo"}
