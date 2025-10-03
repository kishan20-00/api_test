# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["User"]


class User(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    email: str

    created_at: Optional[datetime] = None

    has_redis_profile: Optional[bool] = None

    oauth_id_github: Optional[str] = None

    oauth_id_google: Optional[str] = None

    roles: Optional[List[str]] = None
