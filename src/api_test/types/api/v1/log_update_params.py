# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["LogUpdateParams"]


class LogUpdateParams(TypedDict, total=False):
    endpoint: Required[str]

    request: Required[Dict[str, object]]

    response: Required[Dict[str, object]]

    status_code: Required[int]

    user_id: Optional[str]
