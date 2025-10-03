# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ....types.api.v1 import key_update_params, key_retrieve_params
from ....types.api.v1.key_update_response import KeyUpdateResponse
from ....types.api.v1.key_retrieve_response import KeyRetrieveResponse

__all__ = ["KeysResource", "AsyncKeysResource"]


class KeysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#accessing-raw-response-data-eg-headers
        """
        return KeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#with_streaming_response
        """
        return KeysResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        display_name: str,
        expires_at: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyUpdateResponse:
        """
        Creates a new API key for the current user.

        Args: key_data: The Pydantic model containing the display name and optional
        expiry for the new key. current_user: The authenticated user obtained via
        dependency. key_model: Dependency providing access to the API key database
        model.

        Returns: dict: A dictionary containing the raw, unmasked key (returned only
        once) and the key's metadata.

        Raises: HTTPException: 401 If the user is unauthenticated. HTTPException:
        400/500 If key creation fails due to validation or database error.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/keys/",
            body=maybe_transform(
                {
                    "display_name": display_name,
                    "expires_at": expires_at,
                },
                key_update_params.KeyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyUpdateResponse,
        )

    def delete(
        self,
        key_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Revokes (deactivates) a specific API key belonging to the current user.

        Args: key_id: The ID of the API key to revoke. current_user: The authenticated
        user obtained via dependency. key_model: Dependency providing access to the API
        key database model.

        Returns: None: Returns an empty response with status 204 on successful
        revocation.

        Raises: HTTPException: 401 If the user is unauthenticated. HTTPException: 404 If
        the key is not found or does not belong to the user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/v1/keys/{key_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve(
        self,
        *,
        active_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyRetrieveResponse:
        """
        Retrieves a list of all active or all API keys belonging to the current user,
        including their 24-hour usage statistics.

        Args: current_user: The authenticated user obtained via dependency. key_model:
        Dependency providing access to the API key database model. active_only: Query
        parameter to filter for only active keys. Defaults to True.

        Returns: List[APIKeyResponse]: A list of the user's API key records with added
        usage data.

        Raises: HTTPException: 401 If the user is unauthenticated. HTTPException: 500 If
        fetching keys or usage stats fails.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/keys/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"active_only": active_only}, key_retrieve_params.KeyRetrieveParams),
            ),
            cast_to=KeyRetrieveResponse,
        )


class AsyncKeysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#with_streaming_response
        """
        return AsyncKeysResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        display_name: str,
        expires_at: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyUpdateResponse:
        """
        Creates a new API key for the current user.

        Args: key_data: The Pydantic model containing the display name and optional
        expiry for the new key. current_user: The authenticated user obtained via
        dependency. key_model: Dependency providing access to the API key database
        model.

        Returns: dict: A dictionary containing the raw, unmasked key (returned only
        once) and the key's metadata.

        Raises: HTTPException: 401 If the user is unauthenticated. HTTPException:
        400/500 If key creation fails due to validation or database error.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/keys/",
            body=await async_maybe_transform(
                {
                    "display_name": display_name,
                    "expires_at": expires_at,
                },
                key_update_params.KeyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyUpdateResponse,
        )

    async def delete(
        self,
        key_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Revokes (deactivates) a specific API key belonging to the current user.

        Args: key_id: The ID of the API key to revoke. current_user: The authenticated
        user obtained via dependency. key_model: Dependency providing access to the API
        key database model.

        Returns: None: Returns an empty response with status 204 on successful
        revocation.

        Raises: HTTPException: 401 If the user is unauthenticated. HTTPException: 404 If
        the key is not found or does not belong to the user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/v1/keys/{key_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve(
        self,
        *,
        active_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyRetrieveResponse:
        """
        Retrieves a list of all active or all API keys belonging to the current user,
        including their 24-hour usage statistics.

        Args: current_user: The authenticated user obtained via dependency. key_model:
        Dependency providing access to the API key database model. active_only: Query
        parameter to filter for only active keys. Defaults to True.

        Returns: List[APIKeyResponse]: A list of the user's API key records with added
        usage data.

        Raises: HTTPException: 401 If the user is unauthenticated. HTTPException: 500 If
        fetching keys or usage stats fails.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/keys/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"active_only": active_only}, key_retrieve_params.KeyRetrieveParams),
            ),
            cast_to=KeyRetrieveResponse,
        )


class KeysResourceWithRawResponse:
    def __init__(self, keys: KeysResource) -> None:
        self._keys = keys

        self.update = to_raw_response_wrapper(
            keys.update,
        )
        self.delete = to_raw_response_wrapper(
            keys.delete,
        )
        self.retrieve = to_raw_response_wrapper(
            keys.retrieve,
        )


class AsyncKeysResourceWithRawResponse:
    def __init__(self, keys: AsyncKeysResource) -> None:
        self._keys = keys

        self.update = async_to_raw_response_wrapper(
            keys.update,
        )
        self.delete = async_to_raw_response_wrapper(
            keys.delete,
        )
        self.retrieve = async_to_raw_response_wrapper(
            keys.retrieve,
        )


class KeysResourceWithStreamingResponse:
    def __init__(self, keys: KeysResource) -> None:
        self._keys = keys

        self.update = to_streamed_response_wrapper(
            keys.update,
        )
        self.delete = to_streamed_response_wrapper(
            keys.delete,
        )
        self.retrieve = to_streamed_response_wrapper(
            keys.retrieve,
        )


class AsyncKeysResourceWithStreamingResponse:
    def __init__(self, keys: AsyncKeysResource) -> None:
        self._keys = keys

        self.update = async_to_streamed_response_wrapper(
            keys.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            keys.delete,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            keys.retrieve,
        )
