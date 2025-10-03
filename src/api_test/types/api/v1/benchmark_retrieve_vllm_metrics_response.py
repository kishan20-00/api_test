# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["BenchmarkRetrieveVllmMetricsResponse", "RawMetric"]


class RawMetric(BaseModel):
    name: str

    value: float

    labels: Optional[Dict[str, str]] = None


class BenchmarkRetrieveVllmMetricsResponse(BaseModel):
    api_model_name: str = FieldInfo(alias="model_name")

    timestamp: datetime

    avg_e2e_request_latency_s: Optional[float] = None

    avg_generation_throughput_toks_per_s: Optional[float] = None

    avg_prompt_throughput_toks_per_s: Optional[float] = None

    avg_time_per_output_token_s: Optional[float] = None

    avg_time_to_first_token_s: Optional[float] = None

    cpu_cache_usage_percent: Optional[float] = None

    gpu_cache_usage_percent: Optional[float] = None

    num_requests_running: Optional[int] = None

    num_requests_swapped: Optional[int] = None

    num_requests_waiting: Optional[int] = None

    raw_metrics: Optional[List[RawMetric]] = None

    total_generation_tokens: Optional[int] = None

    total_prompt_tokens: Optional[int] = None

    total_requests_success_abort: Optional[int] = None

    total_requests_success_stop: Optional[int] = None
