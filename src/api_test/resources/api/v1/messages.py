# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ....types.api.v1 import message_update_params
from ....types.api.v1.message import Message

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kishan20-00/api_test#accessing-raw-response-data-eg-headers
        """
        return MessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kishan20-00/api_test#with_streaming_response
        """
        return MessagesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        msg_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Message:
        """
        Retrieves a single message record by its ID.

        Args: msg_id: The ID of the message to retrieve. msg_model: Dependency providing
        access to the message database model.

        Returns: MessageInDB: The requested message record.

        Raises: HTTPException: 404 If no message is found with the given ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not msg_id:
            raise ValueError(f"Expected a non-empty value for `msg_id` but received {msg_id!r}")
        return self._get(
            f"/api/v1/messages/{msg_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )

    def update(
        self,
        msg_id: str,
        *,
        response: Optional[str] | Omit = omit,
        token_count: Optional[int] | Omit = omit,
        token_persecond: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Message:
        """
        Updates an existing message record with new data.

        Args: msg_id: The ID of the message to update. update_data: The Pydantic model
        containing the fields to update. msg_model: Dependency providing access to the
        message database model.

        Returns: MessageInDB: The updated message record.

        Raises: HTTPException: 404 If the message is not found or no changes were made.
        HTTPException: 400 If the update data is invalid.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not msg_id:
            raise ValueError(f"Expected a non-empty value for `msg_id` but received {msg_id!r}")
        return self._patch(
            f"/api/v1/messages/{msg_id}",
            body=maybe_transform(
                {
                    "response": response,
                    "token_count": token_count,
                    "token_persecond": token_persecond,
                },
                message_update_params.MessageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )

    def delete(
        self,
        msg_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a message record by its ID.

        Args: msg_id: The ID of the message to delete. msg_model: Dependency providing
        access to the message database model.

        Returns: None: Returns an empty response with status 204 on successful deletion.

        Raises: HTTPException: 404 If no message is found with the given ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not msg_id:
            raise ValueError(f"Expected a non-empty value for `msg_id` but received {msg_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/v1/messages/{msg_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncMessagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kishan20-00/api_test#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kishan20-00/api_test#with_streaming_response
        """
        return AsyncMessagesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        msg_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Message:
        """
        Retrieves a single message record by its ID.

        Args: msg_id: The ID of the message to retrieve. msg_model: Dependency providing
        access to the message database model.

        Returns: MessageInDB: The requested message record.

        Raises: HTTPException: 404 If no message is found with the given ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not msg_id:
            raise ValueError(f"Expected a non-empty value for `msg_id` but received {msg_id!r}")
        return await self._get(
            f"/api/v1/messages/{msg_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )

    async def update(
        self,
        msg_id: str,
        *,
        response: Optional[str] | Omit = omit,
        token_count: Optional[int] | Omit = omit,
        token_persecond: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Message:
        """
        Updates an existing message record with new data.

        Args: msg_id: The ID of the message to update. update_data: The Pydantic model
        containing the fields to update. msg_model: Dependency providing access to the
        message database model.

        Returns: MessageInDB: The updated message record.

        Raises: HTTPException: 404 If the message is not found or no changes were made.
        HTTPException: 400 If the update data is invalid.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not msg_id:
            raise ValueError(f"Expected a non-empty value for `msg_id` but received {msg_id!r}")
        return await self._patch(
            f"/api/v1/messages/{msg_id}",
            body=await async_maybe_transform(
                {
                    "response": response,
                    "token_count": token_count,
                    "token_persecond": token_persecond,
                },
                message_update_params.MessageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )

    async def delete(
        self,
        msg_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a message record by its ID.

        Args: msg_id: The ID of the message to delete. msg_model: Dependency providing
        access to the message database model.

        Returns: None: Returns an empty response with status 204 on successful deletion.

        Raises: HTTPException: 404 If no message is found with the given ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not msg_id:
            raise ValueError(f"Expected a non-empty value for `msg_id` but received {msg_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/v1/messages/{msg_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.retrieve = to_raw_response_wrapper(
            messages.retrieve,
        )
        self.update = to_raw_response_wrapper(
            messages.update,
        )
        self.delete = to_raw_response_wrapper(
            messages.delete,
        )


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.retrieve = async_to_raw_response_wrapper(
            messages.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            messages.update,
        )
        self.delete = async_to_raw_response_wrapper(
            messages.delete,
        )


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.retrieve = to_streamed_response_wrapper(
            messages.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            messages.update,
        )
        self.delete = to_streamed_response_wrapper(
            messages.delete,
        )


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.retrieve = async_to_streamed_response_wrapper(
            messages.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            messages.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            messages.delete,
        )
