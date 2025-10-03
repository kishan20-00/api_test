# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Mapping, Iterable, cast

import httpx

from ....._types import Body, Query, Headers, NotGiven, FileTypes, not_given
from ....._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.api.v1.files import multipart_init_params, multipart_abort_params, multipart_complete_params

__all__ = ["MultipartResource", "AsyncMultipartResource"]


class MultipartResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MultipartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#accessing-raw-response-data-eg-headers
        """
        return MultipartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MultipartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#with_streaming_response
        """
        return MultipartResourceWithStreamingResponse(self)

    def abort(
        self,
        *,
        upload_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Aborts an in-progress multipart upload in S3 and updates the file record status
        to 'pending'.

        Args: request: Contains upload ID to abort. service: Injected storage service
        dependency. model: Injected database model dependency. current_user: The
        authenticated user obtained via dependency.

        Returns: dict: The result of the S3 abort operation.

        Raises: HTTPException: 500 If the abort operation or metadata update fails.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/files/multipart/abort",
            body=maybe_transform({"upload_id": upload_id}, multipart_abort_params.MultipartAbortParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def complete(
        self,
        *,
        file_name: str,
        parts: Iterable[Dict[str, object]],
        upload_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Completes a multipart upload by combining all uploaded parts in S3.

        Also updates
        the file record status to 'uploaded'.

        Args: request: Contains file name, upload ID, and list of uploaded parts.
        service: Injected storage service dependency. model: Injected database model
        dependency. current_user: The authenticated user obtained via dependency.

        Returns: FileOut: The updated file metadata record.

        Raises: HTTPException: 500 If the S3 operation or metadata update fails.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/files/multipart/complete",
            body=maybe_transform(
                {
                    "file_name": file_name,
                    "parts": parts,
                    "upload_id": upload_id,
                },
                multipart_complete_params.MultipartCompleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def init(
        self,
        *,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Initializes a multipart upload process for large files.

        Generates presigned part
        URLs and creates a preliminary file record in the database.

        Args: file: User uploaded file metadata (not content). service: Injected storage
        service dependency. model: Injected database model dependency. current_user: The
        authenticated user obtained via dependency.

        Returns: dict: The upload ID, file metadata ID, and presigned URLs for parts.

        Raises: HTTPException: 500 If the initialization or metadata storage fails.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/api/v1/files/multipart/init",
            body=maybe_transform(body, multipart_init_params.MultipartInitParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncMultipartResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMultipartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMultipartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMultipartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#with_streaming_response
        """
        return AsyncMultipartResourceWithStreamingResponse(self)

    async def abort(
        self,
        *,
        upload_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Aborts an in-progress multipart upload in S3 and updates the file record status
        to 'pending'.

        Args: request: Contains upload ID to abort. service: Injected storage service
        dependency. model: Injected database model dependency. current_user: The
        authenticated user obtained via dependency.

        Returns: dict: The result of the S3 abort operation.

        Raises: HTTPException: 500 If the abort operation or metadata update fails.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/files/multipart/abort",
            body=await async_maybe_transform({"upload_id": upload_id}, multipart_abort_params.MultipartAbortParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def complete(
        self,
        *,
        file_name: str,
        parts: Iterable[Dict[str, object]],
        upload_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Completes a multipart upload by combining all uploaded parts in S3.

        Also updates
        the file record status to 'uploaded'.

        Args: request: Contains file name, upload ID, and list of uploaded parts.
        service: Injected storage service dependency. model: Injected database model
        dependency. current_user: The authenticated user obtained via dependency.

        Returns: FileOut: The updated file metadata record.

        Raises: HTTPException: 500 If the S3 operation or metadata update fails.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/files/multipart/complete",
            body=await async_maybe_transform(
                {
                    "file_name": file_name,
                    "parts": parts,
                    "upload_id": upload_id,
                },
                multipart_complete_params.MultipartCompleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def init(
        self,
        *,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Initializes a multipart upload process for large files.

        Generates presigned part
        URLs and creates a preliminary file record in the database.

        Args: file: User uploaded file metadata (not content). service: Injected storage
        service dependency. model: Injected database model dependency. current_user: The
        authenticated user obtained via dependency.

        Returns: dict: The upload ID, file metadata ID, and presigned URLs for parts.

        Raises: HTTPException: 500 If the initialization or metadata storage fails.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/api/v1/files/multipart/init",
            body=await async_maybe_transform(body, multipart_init_params.MultipartInitParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class MultipartResourceWithRawResponse:
    def __init__(self, multipart: MultipartResource) -> None:
        self._multipart = multipart

        self.abort = to_raw_response_wrapper(
            multipart.abort,
        )
        self.complete = to_raw_response_wrapper(
            multipart.complete,
        )
        self.init = to_raw_response_wrapper(
            multipart.init,
        )


class AsyncMultipartResourceWithRawResponse:
    def __init__(self, multipart: AsyncMultipartResource) -> None:
        self._multipart = multipart

        self.abort = async_to_raw_response_wrapper(
            multipart.abort,
        )
        self.complete = async_to_raw_response_wrapper(
            multipart.complete,
        )
        self.init = async_to_raw_response_wrapper(
            multipart.init,
        )


class MultipartResourceWithStreamingResponse:
    def __init__(self, multipart: MultipartResource) -> None:
        self._multipart = multipart

        self.abort = to_streamed_response_wrapper(
            multipart.abort,
        )
        self.complete = to_streamed_response_wrapper(
            multipart.complete,
        )
        self.init = to_streamed_response_wrapper(
            multipart.init,
        )


class AsyncMultipartResourceWithStreamingResponse:
    def __init__(self, multipart: AsyncMultipartResource) -> None:
        self._multipart = multipart

        self.abort = async_to_streamed_response_wrapper(
            multipart.abort,
        )
        self.complete = async_to_streamed_response_wrapper(
            multipart.complete,
        )
        self.init = async_to_streamed_response_wrapper(
            multipart.init,
        )
