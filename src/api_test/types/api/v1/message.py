# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["Message"]


class Message(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    conversation_id: str

    is_stream: bool

    latency: str

    api_model_id: str = FieldInfo(alias="model_id")

    prompt: str

    response: str

    token_count: int

    token_persecond: float

    user_id: str

    timestamp: Optional[datetime] = None
