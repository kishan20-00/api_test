# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.auth import token_exchange_params
from ..._base_client import make_request_options
from ...types.token_response import TokenResponse

__all__ = ["TokenResource", "AsyncTokenResource"]


class TokenResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TokenResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#accessing-raw-response-data-eg-headers
        """
        return TokenResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TokenResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#with_streaming_response
        """
        return TokenResourceWithStreamingResponse(self)

    def exchange(
        self,
        *,
        auth_code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenResponse:
        """
        Exchanges a temporary, short-lived JWT authentication code for a full set of
        access and refresh tokens.

        Args: response: The FastAPI response object used to set the HTTP-only refresh
        token cookie. auth_code: The temporary JWT token received from the OAuth
        callback endpoint. user_model: Dependency for accessing the User database model.

        Returns: TokenResponse: A Pydantic model containing the new access token and
        token type.

        Raises: 401 Unauthorized: if not user_id 401 Unauthorized: if not user 401
        Unauthorized: if jwt.ExpiredSignatureError 401 Unauthorized: if jwt.PyJWTError
        500 Internal Server Error: if Exception

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/auth/token/exchange",
            body=maybe_transform({"auth_code": auth_code}, token_exchange_params.TokenExchangeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenResponse,
        )

    def refresh(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenResponse:
        """
        Uses the refresh token stored in an HTTP-only cookie to issue a new access token
        and refresh token pair.

        Args: fastapi_request: The FastAPI request object containing cookies. response:
        The FastAPI response object used to set the new HTTP-only refresh token cookie.
        user_model: Dependency for accessing the User database model.

        Returns: TokenResponse: A Pydantic model containing the new access token and
        token type.

        Raises: 401 Unauthorized: if not refresh_token_cookie 401 Unauthorized: if not
        refresh_payload 401 Unauthorized: if not user_id 401 Unauthorized: if not user
        401 Unauthorized: if HTTPException raised by verify_refresh_token 500 Internal
        Server Error: if Exception
        """
        return self._post(
            "/auth/token/refresh",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenResponse,
        )


class AsyncTokenResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTokenResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTokenResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTokenResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#with_streaming_response
        """
        return AsyncTokenResourceWithStreamingResponse(self)

    async def exchange(
        self,
        *,
        auth_code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenResponse:
        """
        Exchanges a temporary, short-lived JWT authentication code for a full set of
        access and refresh tokens.

        Args: response: The FastAPI response object used to set the HTTP-only refresh
        token cookie. auth_code: The temporary JWT token received from the OAuth
        callback endpoint. user_model: Dependency for accessing the User database model.

        Returns: TokenResponse: A Pydantic model containing the new access token and
        token type.

        Raises: 401 Unauthorized: if not user_id 401 Unauthorized: if not user 401
        Unauthorized: if jwt.ExpiredSignatureError 401 Unauthorized: if jwt.PyJWTError
        500 Internal Server Error: if Exception

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/auth/token/exchange",
            body=await async_maybe_transform({"auth_code": auth_code}, token_exchange_params.TokenExchangeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenResponse,
        )

    async def refresh(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenResponse:
        """
        Uses the refresh token stored in an HTTP-only cookie to issue a new access token
        and refresh token pair.

        Args: fastapi_request: The FastAPI request object containing cookies. response:
        The FastAPI response object used to set the new HTTP-only refresh token cookie.
        user_model: Dependency for accessing the User database model.

        Returns: TokenResponse: A Pydantic model containing the new access token and
        token type.

        Raises: 401 Unauthorized: if not refresh_token_cookie 401 Unauthorized: if not
        refresh_payload 401 Unauthorized: if not user_id 401 Unauthorized: if not user
        401 Unauthorized: if HTTPException raised by verify_refresh_token 500 Internal
        Server Error: if Exception
        """
        return await self._post(
            "/auth/token/refresh",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenResponse,
        )


class TokenResourceWithRawResponse:
    def __init__(self, token: TokenResource) -> None:
        self._token = token

        self.exchange = to_raw_response_wrapper(
            token.exchange,
        )
        self.refresh = to_raw_response_wrapper(
            token.refresh,
        )


class AsyncTokenResourceWithRawResponse:
    def __init__(self, token: AsyncTokenResource) -> None:
        self._token = token

        self.exchange = async_to_raw_response_wrapper(
            token.exchange,
        )
        self.refresh = async_to_raw_response_wrapper(
            token.refresh,
        )


class TokenResourceWithStreamingResponse:
    def __init__(self, token: TokenResource) -> None:
        self._token = token

        self.exchange = to_streamed_response_wrapper(
            token.exchange,
        )
        self.refresh = to_streamed_response_wrapper(
            token.refresh,
        )


class AsyncTokenResourceWithStreamingResponse:
    def __init__(self, token: AsyncTokenResource) -> None:
        self._token = token

        self.exchange = async_to_streamed_response_wrapper(
            token.exchange,
        )
        self.refresh = async_to_streamed_response_wrapper(
            token.refresh,
        )
