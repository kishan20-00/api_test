# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["GoogleResource", "AsyncGoogleResource"]


class GoogleResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GoogleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kishan20-00/api_test#accessing-raw-response-data-eg-headers
        """
        return GoogleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GoogleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kishan20-00/api_test#with_streaming_response
        """
        return GoogleResourceWithStreamingResponse(self)

    def callback(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Handles the callback from the Google OAuth server.

        Args: request: The FastAPI Request object containing query parameters and
        session state. response: The FastAPI Response object. users: Dependency
        providing access to the database's User model.

        Returns: RedirectResponse: A response that redirects the user to the frontend
        callback URL with a temporary `auth_code`.

        Raises: HTTPException: 500 If Google OAuth is unconfigured or user processing
        fails. HTTPException: 400 If email is not found or OAuth fails.
        """
        return self._get(
            "/auth/google/callback",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncGoogleResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGoogleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kishan20-00/api_test#accessing-raw-response-data-eg-headers
        """
        return AsyncGoogleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGoogleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kishan20-00/api_test#with_streaming_response
        """
        return AsyncGoogleResourceWithStreamingResponse(self)

    async def callback(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Handles the callback from the Google OAuth server.

        Args: request: The FastAPI Request object containing query parameters and
        session state. response: The FastAPI Response object. users: Dependency
        providing access to the database's User model.

        Returns: RedirectResponse: A response that redirects the user to the frontend
        callback URL with a temporary `auth_code`.

        Raises: HTTPException: 500 If Google OAuth is unconfigured or user processing
        fails. HTTPException: 400 If email is not found or OAuth fails.
        """
        return await self._get(
            "/auth/google/callback",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class GoogleResourceWithRawResponse:
    def __init__(self, google: GoogleResource) -> None:
        self._google = google

        self.callback = to_raw_response_wrapper(
            google.callback,
        )


class AsyncGoogleResourceWithRawResponse:
    def __init__(self, google: AsyncGoogleResource) -> None:
        self._google = google

        self.callback = async_to_raw_response_wrapper(
            google.callback,
        )


class GoogleResourceWithStreamingResponse:
    def __init__(self, google: GoogleResource) -> None:
        self._google = google

        self.callback = to_streamed_response_wrapper(
            google.callback,
        )


class AsyncGoogleResourceWithStreamingResponse:
    def __init__(self, google: AsyncGoogleResource) -> None:
        self._google = google

        self.callback = async_to_streamed_response_wrapper(
            google.callback,
        )
