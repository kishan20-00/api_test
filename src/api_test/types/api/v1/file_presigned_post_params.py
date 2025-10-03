# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FilePresignedPostParams"]


class FilePresignedPostParams(TypedDict, total=False):
    content_type: Required[str]

    file_name: Required[str]
