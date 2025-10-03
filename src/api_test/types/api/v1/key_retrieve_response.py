# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["KeyRetrieveResponse", "KeyRetrieveResponseItem"]


class KeyRetrieveResponseItem(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    display_name: str

    key_prefix: str

    user_id: str

    created_at: Optional[datetime] = None

    expires_at: Optional[datetime] = None

    is_active: Optional[bool] = None

    last_used_at: Optional[datetime] = None

    masked_key: Optional[str] = None

    usage_24h: Optional[int] = None


KeyRetrieveResponse: TypeAlias = List[KeyRetrieveResponseItem]
