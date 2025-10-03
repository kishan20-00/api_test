# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["ExternalBenchmarkRecord"]


class ExternalBenchmarkRecord(BaseModel):
    api_id: str = FieldInfo(alias="_id")
    """Unique identifier for the benchmark record"""

    date_recorded: date
    """Date when the benchmark was recorded"""

    metric_name: str
    """Name of the metric, e.g., output_tokens_per_sec"""

    metric_unit: str
    """Unit of the metric, e.g., toks/s, ms"""

    metric_value: float
    """Value of the metric"""

    api_model_name: str = FieldInfo(alias="model_name")
    """Name of the language model"""

    provider_name: str
    """Provider or company offering the model/hardware"""

    benchmark_source_url: Optional[str] = None
    """URL to the source of the benchmark data"""

    hardware_info: Optional[str] = None
    """Specific hardware used, e.g., NVIDIA L40S, Tenstorrent Grayskull"""

    notes: Optional[str] = None
    """Additional notes about the benchmark"""
