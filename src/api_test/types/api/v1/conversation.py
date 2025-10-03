# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["Conversation"]


class Conversation(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    title: str

    user_id: str

    created_at: Optional[datetime] = None

    last_updated: Optional[datetime] = None
