# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["FileUpdateParams"]


class FileUpdateParams(TypedDict, total=False):
    content_type: Optional[str]

    deleted_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    filename: Optional[str]

    metadata: Optional[Dict[str, object]]

    org_id: Optional[str]

    owner_id: Optional[str]

    s3_bucket: Optional[str]

    s3_key: Optional[str]

    size: Optional[int]

    status: Optional[Literal["pending", "uploaded", "quarantined", "deleted", "in_progress", "failed"]]

    storage_class: Optional[str]

    version: Optional[int]
