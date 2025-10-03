# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["FileListParams"]


class FileListParams(TypedDict, total=False):
    content_type: Optional[str]

    created_from: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """ISO 8601, UTC assumed if no TZ"""

    created_to: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """ISO 8601, UTC assumed if no TZ"""

    filename_contains: Optional[str]
    """Case-insensitive substring match"""

    limit: int

    max_size: Optional[int]

    min_size: Optional[int]

    org_id: Optional[str]

    owner_id: Optional[str]

    skip: int

    status: Optional[Literal["pending", "uploaded", "quarantined", "deleted", "in_progress", "failed"]]
    """If omitted, "deleted" are excluded"""
