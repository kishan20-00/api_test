# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V1GenerateImageParams"]


class V1GenerateImageParams(TypedDict, total=False):
    model: Required[str]

    prompt: Required[str]

    guidance_scale: Optional[float]

    negative_prompt: Optional[str]

    num_inference_steps: Optional[int]

    poll_interval: Optional[float]

    seed: Optional[int]

    api_timeout: Annotated[Optional[int], PropertyInfo(alias="timeout")]
