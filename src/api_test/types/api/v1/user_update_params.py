# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ...._types import SequenceNotStr

__all__ = ["UserUpdateParams"]


class UserUpdateParams(TypedDict, total=False):
    email: Optional[str]

    oauth_id_github: Optional[str]

    oauth_id_google: Optional[str]

    roles: Optional[SequenceNotStr[str]]
