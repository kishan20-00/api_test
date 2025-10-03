# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["V1RetrieveAPIKeyLogsParams"]


class V1RetrieveAPIKeyLogsParams(TypedDict, total=False):
    end_time: int

    only_errors: bool

    page_num: int

    page_size: int

    start_time: int
