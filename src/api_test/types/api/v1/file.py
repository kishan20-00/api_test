# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["File"]


class File(BaseModel):
    content_type: str

    filename: str

    s3_bucket: str

    s3_key: str

    size: int

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    created_at: Optional[datetime] = None

    deleted_at: Optional[datetime] = None

    metadata: Optional[Dict[str, object]] = None

    org_id: Optional[str] = None

    owner_id: Optional[str] = None

    status: Optional[Literal["pending", "uploaded", "quarantined", "deleted", "in_progress", "failed"]] = None

    storage_class: Optional[str] = None

    updated_at: Optional[datetime] = None

    version: Optional[int] = None
