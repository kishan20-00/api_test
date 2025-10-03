# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["V1AudioInferenceResponse"]


class V1AudioInferenceResponse(BaseModel):
    text: str

    duration: Optional[float] = None

    language: Optional[str] = None
