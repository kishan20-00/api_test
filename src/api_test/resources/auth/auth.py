# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from .login import (
    LoginResource,
    AsyncLoginResource,
    LoginResourceWithRawResponse,
    AsyncLoginResourceWithRawResponse,
    LoginResourceWithStreamingResponse,
    AsyncLoginResourceWithStreamingResponse,
)
from .token import (
    TokenResource,
    AsyncTokenResource,
    TokenResourceWithRawResponse,
    AsyncTokenResourceWithRawResponse,
    TokenResourceWithStreamingResponse,
    AsyncTokenResourceWithStreamingResponse,
)
from .github import (
    GitHubResource,
    AsyncGitHubResource,
    GitHubResourceWithRawResponse,
    AsyncGitHubResourceWithRawResponse,
    GitHubResourceWithStreamingResponse,
    AsyncGitHubResourceWithStreamingResponse,
)
from .google import (
    GoogleResource,
    AsyncGoogleResource,
    GoogleResourceWithRawResponse,
    AsyncGoogleResourceWithRawResponse,
    GoogleResourceWithStreamingResponse,
    AsyncGoogleResourceWithStreamingResponse,
)
from ...types import auth_request_magic_link_params, auth_verify_magic_link_token_params
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
from ..._base_client import make_request_options
from ...types.token_response import TokenResponse

__all__ = ["AuthResource", "AsyncAuthResource"]


class AuthResource(SyncAPIResource):
    @cached_property
    def login(self) -> LoginResource:
        return LoginResource(self._client)

    @cached_property
    def github(self) -> GitHubResource:
        return GitHubResource(self._client)

    @cached_property
    def google(self) -> GoogleResource:
        return GoogleResource(self._client)

    @cached_property
    def token(self) -> TokenResource:
        return TokenResource(self._client)

    @cached_property
    def with_raw_response(self) -> AuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kishan20-00/api_test#accessing-raw-response-data-eg-headers
        """
        return AuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kishan20-00/api_test#with_streaming_response
        """
        return AuthResourceWithStreamingResponse(self)

    def logout(
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
        Deletes the refresh token from the client's cookies and invalidates the
        corresponding entry in Redis.

        Args: response: The FastAPI response object used to delete the cookie.
        refresh_token_cookie: The refresh token read directly from the 'refresh_token'
        cookie (Optional).

        Returns: dict: A simple success message.
        """
        return self._post(
            "/auth/logout",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def request_magic_link(
        self,
        *,
        body: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        API endpoint to initiate the magic link login process.

        Args: payload: Request body containing the user's email. users: Dependency
        providing access to the database's User model.

        Returns: JSONResponse: A confirmation message on success.

        Raises: HTTPException: 400 If email is missing. HTTPException: 500 If email
        service is unconfigured or sending fails.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/auth/request-magic-link",
            body=maybe_transform(body, auth_request_magic_link_params.AuthRequestMagicLinkParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def verify_magic_link_token(
        self,
        *,
        token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenResponse:
        """
        API endpoint to verify the magic link token and complete the login.

        Args: fastapi_response: The FastAPI response object used to set HTTP-only
        cookies. request_body: Pydantic model containing the magic link JWT token.
        users: Dependency providing access to the database's User model.

        Returns: TokenResponse: A model containing the access token (and other
        metadata).

        Raises: HTTPException: 400 If the token is expired or invalid. HTTPException:
        401 If the token's type is incorrect. HTTPException: 500 If user
        creation/processing fails.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/auth/verify-magic-link-token",
            body=maybe_transform({"token": token}, auth_verify_magic_link_token_params.AuthVerifyMagicLinkTokenParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenResponse,
        )


class AsyncAuthResource(AsyncAPIResource):
    @cached_property
    def login(self) -> AsyncLoginResource:
        return AsyncLoginResource(self._client)

    @cached_property
    def github(self) -> AsyncGitHubResource:
        return AsyncGitHubResource(self._client)

    @cached_property
    def google(self) -> AsyncGoogleResource:
        return AsyncGoogleResource(self._client)

    @cached_property
    def token(self) -> AsyncTokenResource:
        return AsyncTokenResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kishan20-00/api_test#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kishan20-00/api_test#with_streaming_response
        """
        return AsyncAuthResourceWithStreamingResponse(self)

    async def logout(
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
        Deletes the refresh token from the client's cookies and invalidates the
        corresponding entry in Redis.

        Args: response: The FastAPI response object used to delete the cookie.
        refresh_token_cookie: The refresh token read directly from the 'refresh_token'
        cookie (Optional).

        Returns: dict: A simple success message.
        """
        return await self._post(
            "/auth/logout",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def request_magic_link(
        self,
        *,
        body: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        API endpoint to initiate the magic link login process.

        Args: payload: Request body containing the user's email. users: Dependency
        providing access to the database's User model.

        Returns: JSONResponse: A confirmation message on success.

        Raises: HTTPException: 400 If email is missing. HTTPException: 500 If email
        service is unconfigured or sending fails.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/auth/request-magic-link",
            body=await async_maybe_transform(body, auth_request_magic_link_params.AuthRequestMagicLinkParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def verify_magic_link_token(
        self,
        *,
        token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenResponse:
        """
        API endpoint to verify the magic link token and complete the login.

        Args: fastapi_response: The FastAPI response object used to set HTTP-only
        cookies. request_body: Pydantic model containing the magic link JWT token.
        users: Dependency providing access to the database's User model.

        Returns: TokenResponse: A model containing the access token (and other
        metadata).

        Raises: HTTPException: 400 If the token is expired or invalid. HTTPException:
        401 If the token's type is incorrect. HTTPException: 500 If user
        creation/processing fails.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/auth/verify-magic-link-token",
            body=await async_maybe_transform(
                {"token": token}, auth_verify_magic_link_token_params.AuthVerifyMagicLinkTokenParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenResponse,
        )


class AuthResourceWithRawResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.logout = to_raw_response_wrapper(
            auth.logout,
        )
        self.request_magic_link = to_raw_response_wrapper(
            auth.request_magic_link,
        )
        self.verify_magic_link_token = to_raw_response_wrapper(
            auth.verify_magic_link_token,
        )

    @cached_property
    def login(self) -> LoginResourceWithRawResponse:
        return LoginResourceWithRawResponse(self._auth.login)

    @cached_property
    def github(self) -> GitHubResourceWithRawResponse:
        return GitHubResourceWithRawResponse(self._auth.github)

    @cached_property
    def google(self) -> GoogleResourceWithRawResponse:
        return GoogleResourceWithRawResponse(self._auth.google)

    @cached_property
    def token(self) -> TokenResourceWithRawResponse:
        return TokenResourceWithRawResponse(self._auth.token)


class AsyncAuthResourceWithRawResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.logout = async_to_raw_response_wrapper(
            auth.logout,
        )
        self.request_magic_link = async_to_raw_response_wrapper(
            auth.request_magic_link,
        )
        self.verify_magic_link_token = async_to_raw_response_wrapper(
            auth.verify_magic_link_token,
        )

    @cached_property
    def login(self) -> AsyncLoginResourceWithRawResponse:
        return AsyncLoginResourceWithRawResponse(self._auth.login)

    @cached_property
    def github(self) -> AsyncGitHubResourceWithRawResponse:
        return AsyncGitHubResourceWithRawResponse(self._auth.github)

    @cached_property
    def google(self) -> AsyncGoogleResourceWithRawResponse:
        return AsyncGoogleResourceWithRawResponse(self._auth.google)

    @cached_property
    def token(self) -> AsyncTokenResourceWithRawResponse:
        return AsyncTokenResourceWithRawResponse(self._auth.token)


class AuthResourceWithStreamingResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.logout = to_streamed_response_wrapper(
            auth.logout,
        )
        self.request_magic_link = to_streamed_response_wrapper(
            auth.request_magic_link,
        )
        self.verify_magic_link_token = to_streamed_response_wrapper(
            auth.verify_magic_link_token,
        )

    @cached_property
    def login(self) -> LoginResourceWithStreamingResponse:
        return LoginResourceWithStreamingResponse(self._auth.login)

    @cached_property
    def github(self) -> GitHubResourceWithStreamingResponse:
        return GitHubResourceWithStreamingResponse(self._auth.github)

    @cached_property
    def google(self) -> GoogleResourceWithStreamingResponse:
        return GoogleResourceWithStreamingResponse(self._auth.google)

    @cached_property
    def token(self) -> TokenResourceWithStreamingResponse:
        return TokenResourceWithStreamingResponse(self._auth.token)


class AsyncAuthResourceWithStreamingResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.logout = async_to_streamed_response_wrapper(
            auth.logout,
        )
        self.request_magic_link = async_to_streamed_response_wrapper(
            auth.request_magic_link,
        )
        self.verify_magic_link_token = async_to_streamed_response_wrapper(
            auth.verify_magic_link_token,
        )

    @cached_property
    def login(self) -> AsyncLoginResourceWithStreamingResponse:
        return AsyncLoginResourceWithStreamingResponse(self._auth.login)

    @cached_property
    def github(self) -> AsyncGitHubResourceWithStreamingResponse:
        return AsyncGitHubResourceWithStreamingResponse(self._auth.github)

    @cached_property
    def google(self) -> AsyncGoogleResourceWithStreamingResponse:
        return AsyncGoogleResourceWithStreamingResponse(self._auth.google)

    @cached_property
    def token(self) -> AsyncTokenResourceWithStreamingResponse:
        return AsyncTokenResourceWithStreamingResponse(self._auth.token)
