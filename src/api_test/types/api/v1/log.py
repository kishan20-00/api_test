# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["Log"]


class Log(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    endpoint: str

    request: Dict[str, object]

    response: Dict[str, object]

    status_code: int

    timestamp: Optional[datetime] = None

    user_id: Optional[str] = None
