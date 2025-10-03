# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .api.v1.user import User

__all__ = ["TokenResponse"]


class TokenResponse(BaseModel):
    access_token: str

    user: User
    """Schema representing a complete user record as stored in the database."""

    token_type: Optional[str] = None
