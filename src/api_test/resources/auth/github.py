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

__all__ = ["GitHubResource", "AsyncGitHubResource"]


class GitHubResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GitHubResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#accessing-raw-response-data-eg-headers
        """
        return GitHubResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GitHubResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#with_streaming_response
        """
        return GitHubResourceWithStreamingResponse(self)

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
        Handles the callback from the GitHub OAuth server.

        Args: request: The FastAPI Request object containing query parameters. response:
        The FastAPI Response object. users: Dependency providing access to the
        database's User model.

        Returns: RedirectResponse: A response that redirects the user to the frontend
        callback URL with a temporary `auth_code`.

        Raises: HTTPException: 500 If GitHub OAuth is unconfigured or user processing
        fails. HTTPException: 400 If no verified primary email is found or OAuth fails.
        """
        return self._get(
            "/auth/github/callback",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncGitHubResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGitHubResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGitHubResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGitHubResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#with_streaming_response
        """
        return AsyncGitHubResourceWithStreamingResponse(self)

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
        Handles the callback from the GitHub OAuth server.

        Args: request: The FastAPI Request object containing query parameters. response:
        The FastAPI Response object. users: Dependency providing access to the
        database's User model.

        Returns: RedirectResponse: A response that redirects the user to the frontend
        callback URL with a temporary `auth_code`.

        Raises: HTTPException: 500 If GitHub OAuth is unconfigured or user processing
        fails. HTTPException: 400 If no verified primary email is found or OAuth fails.
        """
        return await self._get(
            "/auth/github/callback",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class GitHubResourceWithRawResponse:
    def __init__(self, github: GitHubResource) -> None:
        self._github = github

        self.callback = to_raw_response_wrapper(
            github.callback,
        )


class AsyncGitHubResourceWithRawResponse:
    def __init__(self, github: AsyncGitHubResource) -> None:
        self._github = github

        self.callback = async_to_raw_response_wrapper(
            github.callback,
        )


class GitHubResourceWithStreamingResponse:
    def __init__(self, github: GitHubResource) -> None:
        self._github = github

        self.callback = to_streamed_response_wrapper(
            github.callback,
        )


class AsyncGitHubResourceWithStreamingResponse:
    def __init__(self, github: AsyncGitHubResource) -> None:
        self._github = github

        self.callback = async_to_streamed_response_wrapper(
            github.callback,
        )
