from __future__ import annotations

import uuid
from datetime import datetime, timezone


def generate_request_id() -> str:
    return str(uuid.uuid4())


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()
