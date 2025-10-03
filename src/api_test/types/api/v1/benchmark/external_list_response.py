# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .external_benchmark_record import ExternalBenchmarkRecord

__all__ = ["ExternalListResponse"]

ExternalListResponse: TypeAlias = List[ExternalBenchmarkRecord]
