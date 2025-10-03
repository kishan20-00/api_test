# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.api.v1.benchmark import external_create_params
from .....types.api.v1.benchmark.external_list_response import ExternalListResponse
from .....types.api.v1.benchmark.external_benchmark_record import ExternalBenchmarkRecord

__all__ = ["ExternalResource", "AsyncExternalResource"]


class ExternalResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExternalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#accessing-raw-response-data-eg-headers
        """
        return ExternalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExternalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#with_streaming_response
        """
        return ExternalResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        date_recorded: Union[str, date],
        metric_name: str,
        metric_unit: str,
        metric_value: float,
        model_name: str,
        provider_name: str,
        benchmark_source_url: Optional[str] | Omit = omit,
        hardware_info: Optional[str] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalBenchmarkRecord:
        """Adds a new manually curated external benchmark record to the database.

        (Note:
        This endpoint might be protected in a real application)

        Args:
          date_recorded: Date when the benchmark was recorded

          metric_name: Name of the metric, e.g., output_tokens_per_sec

          metric_unit: Unit of the metric, e.g., toks/s, ms

          metric_value: Value of the metric

          model_name: Name of the language model

          provider_name: Provider or company offering the model/hardware

          benchmark_source_url: URL to the source of the benchmark data

          hardware_info: Specific hardware used, e.g., NVIDIA L40S, Tenstorrent Grayskull

          notes: Additional notes about the benchmark

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/benchmark/external",
            body=maybe_transform(
                {
                    "date_recorded": date_recorded,
                    "metric_name": metric_name,
                    "metric_unit": metric_unit,
                    "metric_value": metric_value,
                    "model_name": model_name,
                    "provider_name": provider_name,
                    "benchmark_source_url": benchmark_source_url,
                    "hardware_info": hardware_info,
                    "notes": notes,
                },
                external_create_params.ExternalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalBenchmarkRecord,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalListResponse:
        """Retrieves all manually curated external benchmark records from the database."""
        return self._get(
            "/api/v1/benchmark/external",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalListResponse,
        )


class AsyncExternalResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExternalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExternalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExternalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#with_streaming_response
        """
        return AsyncExternalResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        date_recorded: Union[str, date],
        metric_name: str,
        metric_unit: str,
        metric_value: float,
        model_name: str,
        provider_name: str,
        benchmark_source_url: Optional[str] | Omit = omit,
        hardware_info: Optional[str] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalBenchmarkRecord:
        """Adds a new manually curated external benchmark record to the database.

        (Note:
        This endpoint might be protected in a real application)

        Args:
          date_recorded: Date when the benchmark was recorded

          metric_name: Name of the metric, e.g., output_tokens_per_sec

          metric_unit: Unit of the metric, e.g., toks/s, ms

          metric_value: Value of the metric

          model_name: Name of the language model

          provider_name: Provider or company offering the model/hardware

          benchmark_source_url: URL to the source of the benchmark data

          hardware_info: Specific hardware used, e.g., NVIDIA L40S, Tenstorrent Grayskull

          notes: Additional notes about the benchmark

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/benchmark/external",
            body=await async_maybe_transform(
                {
                    "date_recorded": date_recorded,
                    "metric_name": metric_name,
                    "metric_unit": metric_unit,
                    "metric_value": metric_value,
                    "model_name": model_name,
                    "provider_name": provider_name,
                    "benchmark_source_url": benchmark_source_url,
                    "hardware_info": hardware_info,
                    "notes": notes,
                },
                external_create_params.ExternalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalBenchmarkRecord,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalListResponse:
        """Retrieves all manually curated external benchmark records from the database."""
        return await self._get(
            "/api/v1/benchmark/external",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalListResponse,
        )


class ExternalResourceWithRawResponse:
    def __init__(self, external: ExternalResource) -> None:
        self._external = external

        self.create = to_raw_response_wrapper(
            external.create,
        )
        self.list = to_raw_response_wrapper(
            external.list,
        )


class AsyncExternalResourceWithRawResponse:
    def __init__(self, external: AsyncExternalResource) -> None:
        self._external = external

        self.create = async_to_raw_response_wrapper(
            external.create,
        )
        self.list = async_to_raw_response_wrapper(
            external.list,
        )


class ExternalResourceWithStreamingResponse:
    def __init__(self, external: ExternalResource) -> None:
        self._external = external

        self.create = to_streamed_response_wrapper(
            external.create,
        )
        self.list = to_streamed_response_wrapper(
            external.list,
        )


class AsyncExternalResourceWithStreamingResponse:
    def __init__(self, external: AsyncExternalResource) -> None:
        self._external = external

        self.create = async_to_streamed_response_wrapper(
            external.create,
        )
        self.list = async_to_streamed_response_wrapper(
            external.list,
        )
