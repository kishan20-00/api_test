# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["FileCreateParams"]


class FileCreateParams(TypedDict, total=False):
    content_type: Required[str]

    filename: Required[str]

    s3_bucket: Required[str]

    s3_key: Required[str]

    size: Required[int]

    metadata: Optional[Dict[str, object]]

    org_id: Optional[str]

    owner_id: Optional[str]

    status: Literal["pending", "uploaded", "quarantined", "deleted", "in_progress", "failed"]

    storage_class: Optional[str]

    version: int
