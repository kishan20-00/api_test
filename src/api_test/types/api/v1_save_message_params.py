# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["V1SaveMessageParams"]


class V1SaveMessageParams(TypedDict, total=False):
    is_stream: Required[bool]

    latency: Required[str]

    model_id: Required[str]

    prompt: Required[str]

    response: Required[str]

    token_count: Required[int]

    token_persecond: Required[float]

    conversation_id: Optional[str]
