# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.api.v1.user import User

__all__ = ["DebugResource", "AsyncDebugResource"]


class DebugResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DebugResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#accessing-raw-response-data-eg-headers
        """
        return DebugResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DebugResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#with_streaming_response
        """
        return DebugResourceWithStreamingResponse(self)

    def retrieve_current_user(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Debugging endpoint to retrieve the current authenticated user's details.

        Args: current_user: The authenticated user obtained via dependency.

        Returns: UserInDB: The Pydantic model of the current user.

        Raises: HTTPException: 401 If the user is unauthenticated.
        """
        return self._get(
            "/api/v1/debug/current-user",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )


class AsyncDebugResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDebugResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDebugResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDebugResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#with_streaming_response
        """
        return AsyncDebugResourceWithStreamingResponse(self)

    async def retrieve_current_user(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> User:
        """
        Debugging endpoint to retrieve the current authenticated user's details.

        Args: current_user: The authenticated user obtained via dependency.

        Returns: UserInDB: The Pydantic model of the current user.

        Raises: HTTPException: 401 If the user is unauthenticated.
        """
        return await self._get(
            "/api/v1/debug/current-user",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )


class DebugResourceWithRawResponse:
    def __init__(self, debug: DebugResource) -> None:
        self._debug = debug

        self.retrieve_current_user = to_raw_response_wrapper(
            debug.retrieve_current_user,
        )


class AsyncDebugResourceWithRawResponse:
    def __init__(self, debug: AsyncDebugResource) -> None:
        self._debug = debug

        self.retrieve_current_user = async_to_raw_response_wrapper(
            debug.retrieve_current_user,
        )


class DebugResourceWithStreamingResponse:
    def __init__(self, debug: DebugResource) -> None:
        self._debug = debug

        self.retrieve_current_user = to_streamed_response_wrapper(
            debug.retrieve_current_user,
        )


class AsyncDebugResourceWithStreamingResponse:
    def __init__(self, debug: AsyncDebugResource) -> None:
        self._debug = debug

        self.retrieve_current_user = async_to_streamed_response_wrapper(
            debug.retrieve_current_user,
        )
