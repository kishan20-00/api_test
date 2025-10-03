# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.api.v1 import log_update_params, log_retrieve_params
from ....types.api.v1.log import Log
from ....types.api.v1.log_retrieve_response import LogRetrieveResponse

__all__ = ["LogsResource", "AsyncLogsResource"]


class LogsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#accessing-raw-response-data-eg-headers
        """
        return LogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#with_streaming_response
        """
        return LogsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        endpoint: str,
        *,
        limit: int | Omit = omit,
        skip: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogRetrieveResponse:
        """
        Retrieves a paginated list of logs filtered by a specific endpoint path.

        Args: endpoint: The API endpoint path to filter logs by (e.g.,
        '/v1/chat/completions'). limit: Query parameter for the maximum number of logs
        to return. skip: Query parameter for pagination offset. log_model: Dependency
        providing access to the log database model.

        Returns: List[LogInDB]: A list of log records for the specified endpoint.

        Raises: None (DB errors are handled internally by the model or propagate as
        500).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not endpoint:
            raise ValueError(f"Expected a non-empty value for `endpoint` but received {endpoint!r}")
        return self._get(
            f"/api/v1/logs/endpoint/{endpoint}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                    },
                    log_retrieve_params.LogRetrieveParams,
                ),
            ),
            cast_to=LogRetrieveResponse,
        )

    def update(
        self,
        *,
        endpoint: str,
        request: Dict[str, object],
        response: Dict[str, object],
        status_code: int,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Log:
        """
        Creates a new log entry in the database.

        Args: log_data: The Pydantic model containing the log data (e.g., endpoint,
        request details). log_model: Dependency providing access to the log database
        model.

        Returns: LogInDB: The newly created log record.

        Raises: HTTPException: 400 If the user ID is invalid (propagated from the
        model). HTTPException: 500 For internal server errors during creation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/logs/",
            body=maybe_transform(
                {
                    "endpoint": endpoint,
                    "request": request,
                    "response": response,
                    "status_code": status_code,
                    "user_id": user_id,
                },
                log_update_params.LogUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Log,
        )

    def retrieve(
        self,
        *,
        limit: int | Omit = omit,
        skip: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogRetrieveResponse:
        """
        Retrieves a paginated list of the most recent application logs.

        Args: limit: Query parameter for the maximum number of logs to return. skip:
        Query parameter for pagination offset. log_model: Dependency providing access to
        the log database model.

        Returns: List[LogInDB]: A list of recent log records.

        Raises: None (DB errors are handled internally by the model or propagate as
        500).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/logs/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                    },
                    log_retrieve_params.LogRetrieveParams,
                ),
            ),
            cast_to=LogRetrieveResponse,
        )


class AsyncLogsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#with_streaming_response
        """
        return AsyncLogsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        endpoint: str,
        *,
        limit: int | Omit = omit,
        skip: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogRetrieveResponse:
        """
        Retrieves a paginated list of logs filtered by a specific endpoint path.

        Args: endpoint: The API endpoint path to filter logs by (e.g.,
        '/v1/chat/completions'). limit: Query parameter for the maximum number of logs
        to return. skip: Query parameter for pagination offset. log_model: Dependency
        providing access to the log database model.

        Returns: List[LogInDB]: A list of log records for the specified endpoint.

        Raises: None (DB errors are handled internally by the model or propagate as
        500).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not endpoint:
            raise ValueError(f"Expected a non-empty value for `endpoint` but received {endpoint!r}")
        return await self._get(
            f"/api/v1/logs/endpoint/{endpoint}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                    },
                    log_retrieve_params.LogRetrieveParams,
                ),
            ),
            cast_to=LogRetrieveResponse,
        )

    async def update(
        self,
        *,
        endpoint: str,
        request: Dict[str, object],
        response: Dict[str, object],
        status_code: int,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Log:
        """
        Creates a new log entry in the database.

        Args: log_data: The Pydantic model containing the log data (e.g., endpoint,
        request details). log_model: Dependency providing access to the log database
        model.

        Returns: LogInDB: The newly created log record.

        Raises: HTTPException: 400 If the user ID is invalid (propagated from the
        model). HTTPException: 500 For internal server errors during creation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/logs/",
            body=await async_maybe_transform(
                {
                    "endpoint": endpoint,
                    "request": request,
                    "response": response,
                    "status_code": status_code,
                    "user_id": user_id,
                },
                log_update_params.LogUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Log,
        )

    async def retrieve(
        self,
        *,
        limit: int | Omit = omit,
        skip: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogRetrieveResponse:
        """
        Retrieves a paginated list of the most recent application logs.

        Args: limit: Query parameter for the maximum number of logs to return. skip:
        Query parameter for pagination offset. log_model: Dependency providing access to
        the log database model.

        Returns: List[LogInDB]: A list of recent log records.

        Raises: None (DB errors are handled internally by the model or propagate as
        500).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/logs/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                    },
                    log_retrieve_params.LogRetrieveParams,
                ),
            ),
            cast_to=LogRetrieveResponse,
        )


class LogsResourceWithRawResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

        self.retrieve = to_raw_response_wrapper(
            logs.retrieve,
        )
        self.update = to_raw_response_wrapper(
            logs.update,
        )
        self.retrieve = to_raw_response_wrapper(
            logs.retrieve,
        )


class AsyncLogsResourceWithRawResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

        self.retrieve = async_to_raw_response_wrapper(
            logs.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            logs.update,
        )
        self.retrieve = async_to_raw_response_wrapper(
            logs.retrieve,
        )


class LogsResourceWithStreamingResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

        self.retrieve = to_streamed_response_wrapper(
            logs.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            logs.update,
        )
        self.retrieve = to_streamed_response_wrapper(
            logs.retrieve,
        )


class AsyncLogsResourceWithStreamingResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

        self.retrieve = async_to_streamed_response_wrapper(
            logs.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            logs.update,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            logs.retrieve,
        )
