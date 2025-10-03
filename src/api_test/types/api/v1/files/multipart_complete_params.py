# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["MultipartCompleteParams"]


class MultipartCompleteParams(TypedDict, total=False):
    file_name: Required[str]

    parts: Required[Iterable[Dict[str, object]]]

    upload_id: Required[str]
