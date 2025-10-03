# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .external import (
    ExternalResource,
    AsyncExternalResource,
    ExternalResourceWithRawResponse,
    AsyncExternalResourceWithRawResponse,
    ExternalResourceWithStreamingResponse,
    AsyncExternalResourceWithStreamingResponse,
)
from ....._types import Body, Query, Headers, NotGiven, not_given
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.api.v1.benchmark_retrieve_vllm_metrics_response import BenchmarkRetrieveVllmMetricsResponse

__all__ = ["BenchmarkResource", "AsyncBenchmarkResource"]


class BenchmarkResource(SyncAPIResource):
    @cached_property
    def external(self) -> ExternalResource:
        return ExternalResource(self._client)

    @cached_property
    def with_raw_response(self) -> BenchmarkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#accessing-raw-response-data-eg-headers
        """
        return BenchmarkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BenchmarkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#with_streaming_response
        """
        return BenchmarkResourceWithStreamingResponse(self)

    def retrieve_vllm_metrics(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BenchmarkRetrieveVllmMetricsResponse:
        """
        Fetches the latest performance metrics from the configured vLLM, processes them,
        and returns a snapshot.
        """
        return self._get(
            "/api/v1/benchmark/vllm-metrics",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BenchmarkRetrieveVllmMetricsResponse,
        )


class AsyncBenchmarkResource(AsyncAPIResource):
    @cached_property
    def external(self) -> AsyncExternalResource:
        return AsyncExternalResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBenchmarkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBenchmarkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBenchmarkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#with_streaming_response
        """
        return AsyncBenchmarkResourceWithStreamingResponse(self)

    async def retrieve_vllm_metrics(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BenchmarkRetrieveVllmMetricsResponse:
        """
        Fetches the latest performance metrics from the configured vLLM, processes them,
        and returns a snapshot.
        """
        return await self._get(
            "/api/v1/benchmark/vllm-metrics",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BenchmarkRetrieveVllmMetricsResponse,
        )


class BenchmarkResourceWithRawResponse:
    def __init__(self, benchmark: BenchmarkResource) -> None:
        self._benchmark = benchmark

        self.retrieve_vllm_metrics = to_raw_response_wrapper(
            benchmark.retrieve_vllm_metrics,
        )

    @cached_property
    def external(self) -> ExternalResourceWithRawResponse:
        return ExternalResourceWithRawResponse(self._benchmark.external)


class AsyncBenchmarkResourceWithRawResponse:
    def __init__(self, benchmark: AsyncBenchmarkResource) -> None:
        self._benchmark = benchmark

        self.retrieve_vllm_metrics = async_to_raw_response_wrapper(
            benchmark.retrieve_vllm_metrics,
        )

    @cached_property
    def external(self) -> AsyncExternalResourceWithRawResponse:
        return AsyncExternalResourceWithRawResponse(self._benchmark.external)


class BenchmarkResourceWithStreamingResponse:
    def __init__(self, benchmark: BenchmarkResource) -> None:
        self._benchmark = benchmark

        self.retrieve_vllm_metrics = to_streamed_response_wrapper(
            benchmark.retrieve_vllm_metrics,
        )

    @cached_property
    def external(self) -> ExternalResourceWithStreamingResponse:
        return ExternalResourceWithStreamingResponse(self._benchmark.external)


class AsyncBenchmarkResourceWithStreamingResponse:
    def __init__(self, benchmark: AsyncBenchmarkResource) -> None:
        self._benchmark = benchmark

        self.retrieve_vllm_metrics = async_to_streamed_response_wrapper(
            benchmark.retrieve_vllm_metrics,
        )

    @cached_property
    def external(self) -> AsyncExternalResourceWithStreamingResponse:
        return AsyncExternalResourceWithStreamingResponse(self._benchmark.external)
