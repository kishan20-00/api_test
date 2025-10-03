# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ExternalCreateParams"]


class ExternalCreateParams(TypedDict, total=False):
    date_recorded: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Date when the benchmark was recorded"""

    metric_name: Required[str]
    """Name of the metric, e.g., output_tokens_per_sec"""

    metric_unit: Required[str]
    """Unit of the metric, e.g., toks/s, ms"""

    metric_value: Required[float]
    """Value of the metric"""

    model_name: Required[str]
    """Name of the language model"""

    provider_name: Required[str]
    """Provider or company offering the model/hardware"""

    benchmark_source_url: Optional[str]
    """URL to the source of the benchmark data"""

    hardware_info: Optional[str]
    """Specific hardware used, e.g., NVIDIA L40S, Tenstorrent Grayskull"""

    notes: Optional[str]
    """Additional notes about the benchmark"""
