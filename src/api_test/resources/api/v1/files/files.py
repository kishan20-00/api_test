# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from .multipart import (
    MultipartResource,
    AsyncMultipartResource,
    MultipartResourceWithRawResponse,
    AsyncMultipartResourceWithRawResponse,
    MultipartResourceWithStreamingResponse,
    AsyncMultipartResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.api.v1 import (
    file_list_params,
    file_create_params,
    file_update_params,
    file_presigned_post_params,
    file_retrieve_download_params,
)
from .....types.api.v1.file import File
from .....types.api.v1.file_list_response import FileListResponse

__all__ = ["FilesResource", "AsyncFilesResource"]


class FilesResource(SyncAPIResource):
    @cached_property
    def multipart(self) -> MultipartResource:
        return MultipartResource(self._client)

    @cached_property
    def with_raw_response(self) -> FilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kishan20-00/api_test#accessing-raw-response-data-eg-headers
        """
        return FilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kishan20-00/api_test#with_streaming_response
        """
        return FilesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        content_type: str,
        filename: str,
        s3_bucket: str,
        s3_key: str,
        size: int,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        org_id: Optional[str] | Omit = omit,
        owner_id: Optional[str] | Omit = omit,
        status: Literal["pending", "uploaded", "quarantined", "deleted", "in_progress", "failed"] | Omit = omit,
        storage_class: Optional[str] | Omit = omit,
        version: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Creates a new file metadata record in the database after the file has been
        uploaded externally.

        Args: payload: File metadata details to create. model: Dependency providing
        access to the storage database model. current_user: The authenticated user
        obtained via dependency.

        Returns: FileOut: The newly created file metadata record.

        Raises: HTTPException: 400 If required fields are missing or constraints are
        violated.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/files",
            body=maybe_transform(
                {
                    "content_type": content_type,
                    "filename": filename,
                    "s3_bucket": s3_bucket,
                    "s3_key": s3_key,
                    "size": size,
                    "metadata": metadata,
                    "org_id": org_id,
                    "owner_id": owner_id,
                    "status": status,
                    "storage_class": storage_class,
                    "version": version,
                },
                file_create_params.FileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=File,
        )

    def retrieve(
        self,
        key: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Retrieves metadata directly from S3 for a specific object key.

        Args: key: S3 object key of the file. service: Injected storage service
        dependency. current_user: The authenticated user obtained via dependency.

        Returns: dict: S3 object metadata.

        Raises: HTTPException: 404 If the key is not found in S3.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return self._get(
            f"/api/v1/files/s3/{key}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def update(
        self,
        file_id: str,
        *,
        content_type: Optional[str] | Omit = omit,
        deleted_at: Union[str, datetime, None] | Omit = omit,
        filename: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        org_id: Optional[str] | Omit = omit,
        owner_id: Optional[str] | Omit = omit,
        s3_bucket: Optional[str] | Omit = omit,
        s3_key: Optional[str] | Omit = omit,
        size: Optional[int] | Omit = omit,
        status: Optional[Literal["pending", "uploaded", "quarantined", "deleted", "in_progress", "failed"]]
        | Omit = omit,
        storage_class: Optional[str] | Omit = omit,
        version: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Updates an existing file metadata record by its ID.

        Args: fileId: Identifier of the file metadata record. payload: Metadata fields
        to update. model: Dependency providing access to the storage database model.
        current_user: The authenticated user obtained via dependency.

        Returns: FileOut: The updated file metadata record.

        Raises: HTTPException: 404 If the file ID is not found. HTTPException: 400 If
        the update payload is invalid.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._patch(
            f"/api/v1/files/{file_id}",
            body=maybe_transform(
                {
                    "content_type": content_type,
                    "deleted_at": deleted_at,
                    "filename": filename,
                    "metadata": metadata,
                    "org_id": org_id,
                    "owner_id": owner_id,
                    "s3_bucket": s3_bucket,
                    "s3_key": s3_key,
                    "size": size,
                    "status": status,
                    "storage_class": storage_class,
                    "version": version,
                },
                file_update_params.FileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=File,
        )

    def list(
        self,
        *,
        content_type: Optional[str] | Omit = omit,
        created_from: Union[str, datetime, None] | Omit = omit,
        created_to: Union[str, datetime, None] | Omit = omit,
        filename_contains: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        max_size: Optional[int] | Omit = omit,
        min_size: Optional[int] | Omit = omit,
        org_id: Optional[str] | Omit = omit,
        owner_id: Optional[str] | Omit = omit,
        skip: int | Omit = omit,
        status: Optional[Literal["pending", "uploaded", "quarantined", "deleted", "in_progress", "failed"]]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileListResponse:
        """
        Retrieves a paginated list of file metadata records, supporting various
        filtering options.

        Args: limit: Query parameter for pagination size. skip: Query parameter for
        pagination offset. owner_id: Filter by file owner ID. org_id: Filter by
        organization ID. status: Filter by file status. content_type: Filter by file
        MIME type. filename_contains: Filter by filename substring. created_from: Filter
        for files created after this date. created_to: Filter for files created before
        this date. min_size: Filter for minimum size. max_size: Filter for maximum size.
        model: Dependency providing access to the storage database model. current_user:
        The authenticated user obtained via dependency.

        Returns: FileListResponse: The list of files, total count, and pagination info.

        Raises: HTTPException: 500 If the listing fails.

        Args:
          created_from: ISO 8601, UTC assumed if no TZ

          created_to: ISO 8601, UTC assumed if no TZ

          filename_contains: Case-insensitive substring match

          status: If omitted, "deleted" are excluded

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "content_type": content_type,
                        "created_from": created_from,
                        "created_to": created_to,
                        "filename_contains": filename_contains,
                        "limit": limit,
                        "max_size": max_size,
                        "min_size": min_size,
                        "org_id": org_id,
                        "owner_id": owner_id,
                        "skip": skip,
                        "status": status,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            cast_to=FileListResponse,
        )

    def delete(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Performs a soft delete on a file metadata record by marking it as 'deleted'.

        The
        actual file content in S3 is retained.

        Args: fileId: Identifier of the file to soft delete. model: Dependency providing
        access to the storage database model. current_user: The authenticated user
        obtained via dependency.

        Returns: dict: A confirmation dictionary.

        Raises: HTTPException: 404 If the file is not found or already deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._delete(
            f"/api/v1/files/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def delete_purge(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Permanently deletes a file from S3 and removes its metadata record from the
        database.

        Args: fileId: The ID of the file to be permanently deleted. service: Injected
        storage service dependency. model: Injected database model dependency.
        current_user: The authenticated user dependency.

        Returns: dict: Confirmation of the deletion.

        Raises: HTTPException: 404 If the file is not found. HTTPException: 500 If the
        deletion fails unexpectedly.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._delete(
            f"/api/v1/files/{file_id}/purge",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def presigned_post(
        self,
        *,
        content_type: str,
        file_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Generates a presigned POST request for securely uploading files directly to S3
        from a client.

        Args: request: FastAPI request context. file_name: Desired name of the file in
        S3. content_type: MIME type of the file. service: Injected storage service
        dependency. current_user: The authenticated user obtained via dependency.

        Returns: dict: The presigned URL and form fields required for the direct upload.

        Raises: HTTPException: 500 If the presigned URL generation fails.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/files/presigned-post",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "content_type": content_type,
                        "file_name": file_name,
                    },
                    file_presigned_post_params.FilePresignedPostParams,
                ),
            ),
            cast_to=object,
        )

    def retrieve_download(
        self,
        file_id: str,
        *,
        choice: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Generates a presigned URL for downloading or uploading a file based on the S3
        key.

        Args: file_id: Identifier (S3 key) of the file. choice: Operation type
        ("get_object" or "put_object"). service: Injected storage service dependency.
        current_user: The authenticated user obtained via dependency.

        Returns: dict: The presigned URL.

        Raises: HTTPException: 500 If the presigned URL generation fails.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._get(
            f"/api/v1/files/{file_id}/download",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"choice": choice}, file_retrieve_download_params.FileRetrieveDownloadParams),
            ),
            cast_to=object,
        )


class AsyncFilesResource(AsyncAPIResource):
    @cached_property
    def multipart(self) -> AsyncMultipartResource:
        return AsyncMultipartResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kishan20-00/api_test#accessing-raw-response-data-eg-headers
        """
        return AsyncFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kishan20-00/api_test#with_streaming_response
        """
        return AsyncFilesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        content_type: str,
        filename: str,
        s3_bucket: str,
        s3_key: str,
        size: int,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        org_id: Optional[str] | Omit = omit,
        owner_id: Optional[str] | Omit = omit,
        status: Literal["pending", "uploaded", "quarantined", "deleted", "in_progress", "failed"] | Omit = omit,
        storage_class: Optional[str] | Omit = omit,
        version: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Creates a new file metadata record in the database after the file has been
        uploaded externally.

        Args: payload: File metadata details to create. model: Dependency providing
        access to the storage database model. current_user: The authenticated user
        obtained via dependency.

        Returns: FileOut: The newly created file metadata record.

        Raises: HTTPException: 400 If required fields are missing or constraints are
        violated.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/files",
            body=await async_maybe_transform(
                {
                    "content_type": content_type,
                    "filename": filename,
                    "s3_bucket": s3_bucket,
                    "s3_key": s3_key,
                    "size": size,
                    "metadata": metadata,
                    "org_id": org_id,
                    "owner_id": owner_id,
                    "status": status,
                    "storage_class": storage_class,
                    "version": version,
                },
                file_create_params.FileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=File,
        )

    async def retrieve(
        self,
        key: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Retrieves metadata directly from S3 for a specific object key.

        Args: key: S3 object key of the file. service: Injected storage service
        dependency. current_user: The authenticated user obtained via dependency.

        Returns: dict: S3 object metadata.

        Raises: HTTPException: 404 If the key is not found in S3.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return await self._get(
            f"/api/v1/files/s3/{key}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def update(
        self,
        file_id: str,
        *,
        content_type: Optional[str] | Omit = omit,
        deleted_at: Union[str, datetime, None] | Omit = omit,
        filename: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        org_id: Optional[str] | Omit = omit,
        owner_id: Optional[str] | Omit = omit,
        s3_bucket: Optional[str] | Omit = omit,
        s3_key: Optional[str] | Omit = omit,
        size: Optional[int] | Omit = omit,
        status: Optional[Literal["pending", "uploaded", "quarantined", "deleted", "in_progress", "failed"]]
        | Omit = omit,
        storage_class: Optional[str] | Omit = omit,
        version: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Updates an existing file metadata record by its ID.

        Args: fileId: Identifier of the file metadata record. payload: Metadata fields
        to update. model: Dependency providing access to the storage database model.
        current_user: The authenticated user obtained via dependency.

        Returns: FileOut: The updated file metadata record.

        Raises: HTTPException: 404 If the file ID is not found. HTTPException: 400 If
        the update payload is invalid.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._patch(
            f"/api/v1/files/{file_id}",
            body=await async_maybe_transform(
                {
                    "content_type": content_type,
                    "deleted_at": deleted_at,
                    "filename": filename,
                    "metadata": metadata,
                    "org_id": org_id,
                    "owner_id": owner_id,
                    "s3_bucket": s3_bucket,
                    "s3_key": s3_key,
                    "size": size,
                    "status": status,
                    "storage_class": storage_class,
                    "version": version,
                },
                file_update_params.FileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=File,
        )

    async def list(
        self,
        *,
        content_type: Optional[str] | Omit = omit,
        created_from: Union[str, datetime, None] | Omit = omit,
        created_to: Union[str, datetime, None] | Omit = omit,
        filename_contains: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        max_size: Optional[int] | Omit = omit,
        min_size: Optional[int] | Omit = omit,
        org_id: Optional[str] | Omit = omit,
        owner_id: Optional[str] | Omit = omit,
        skip: int | Omit = omit,
        status: Optional[Literal["pending", "uploaded", "quarantined", "deleted", "in_progress", "failed"]]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileListResponse:
        """
        Retrieves a paginated list of file metadata records, supporting various
        filtering options.

        Args: limit: Query parameter for pagination size. skip: Query parameter for
        pagination offset. owner_id: Filter by file owner ID. org_id: Filter by
        organization ID. status: Filter by file status. content_type: Filter by file
        MIME type. filename_contains: Filter by filename substring. created_from: Filter
        for files created after this date. created_to: Filter for files created before
        this date. min_size: Filter for minimum size. max_size: Filter for maximum size.
        model: Dependency providing access to the storage database model. current_user:
        The authenticated user obtained via dependency.

        Returns: FileListResponse: The list of files, total count, and pagination info.

        Raises: HTTPException: 500 If the listing fails.

        Args:
          created_from: ISO 8601, UTC assumed if no TZ

          created_to: ISO 8601, UTC assumed if no TZ

          filename_contains: Case-insensitive substring match

          status: If omitted, "deleted" are excluded

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "content_type": content_type,
                        "created_from": created_from,
                        "created_to": created_to,
                        "filename_contains": filename_contains,
                        "limit": limit,
                        "max_size": max_size,
                        "min_size": min_size,
                        "org_id": org_id,
                        "owner_id": owner_id,
                        "skip": skip,
                        "status": status,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            cast_to=FileListResponse,
        )

    async def delete(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Performs a soft delete on a file metadata record by marking it as 'deleted'.

        The
        actual file content in S3 is retained.

        Args: fileId: Identifier of the file to soft delete. model: Dependency providing
        access to the storage database model. current_user: The authenticated user
        obtained via dependency.

        Returns: dict: A confirmation dictionary.

        Raises: HTTPException: 404 If the file is not found or already deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._delete(
            f"/api/v1/files/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def delete_purge(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Permanently deletes a file from S3 and removes its metadata record from the
        database.

        Args: fileId: The ID of the file to be permanently deleted. service: Injected
        storage service dependency. model: Injected database model dependency.
        current_user: The authenticated user dependency.

        Returns: dict: Confirmation of the deletion.

        Raises: HTTPException: 404 If the file is not found. HTTPException: 500 If the
        deletion fails unexpectedly.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._delete(
            f"/api/v1/files/{file_id}/purge",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def presigned_post(
        self,
        *,
        content_type: str,
        file_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Generates a presigned POST request for securely uploading files directly to S3
        from a client.

        Args: request: FastAPI request context. file_name: Desired name of the file in
        S3. content_type: MIME type of the file. service: Injected storage service
        dependency. current_user: The authenticated user obtained via dependency.

        Returns: dict: The presigned URL and form fields required for the direct upload.

        Raises: HTTPException: 500 If the presigned URL generation fails.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/files/presigned-post",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "content_type": content_type,
                        "file_name": file_name,
                    },
                    file_presigned_post_params.FilePresignedPostParams,
                ),
            ),
            cast_to=object,
        )

    async def retrieve_download(
        self,
        file_id: str,
        *,
        choice: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Generates a presigned URL for downloading or uploading a file based on the S3
        key.

        Args: file_id: Identifier (S3 key) of the file. choice: Operation type
        ("get_object" or "put_object"). service: Injected storage service dependency.
        current_user: The authenticated user obtained via dependency.

        Returns: dict: The presigned URL.

        Raises: HTTPException: 500 If the presigned URL generation fails.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._get(
            f"/api/v1/files/{file_id}/download",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"choice": choice}, file_retrieve_download_params.FileRetrieveDownloadParams
                ),
            ),
            cast_to=object,
        )


class FilesResourceWithRawResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.create = to_raw_response_wrapper(
            files.create,
        )
        self.retrieve = to_raw_response_wrapper(
            files.retrieve,
        )
        self.update = to_raw_response_wrapper(
            files.update,
        )
        self.list = to_raw_response_wrapper(
            files.list,
        )
        self.delete = to_raw_response_wrapper(
            files.delete,
        )
        self.delete_purge = to_raw_response_wrapper(
            files.delete_purge,
        )
        self.presigned_post = to_raw_response_wrapper(
            files.presigned_post,
        )
        self.retrieve_download = to_raw_response_wrapper(
            files.retrieve_download,
        )

    @cached_property
    def multipart(self) -> MultipartResourceWithRawResponse:
        return MultipartResourceWithRawResponse(self._files.multipart)


class AsyncFilesResourceWithRawResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.create = async_to_raw_response_wrapper(
            files.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            files.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            files.update,
        )
        self.list = async_to_raw_response_wrapper(
            files.list,
        )
        self.delete = async_to_raw_response_wrapper(
            files.delete,
        )
        self.delete_purge = async_to_raw_response_wrapper(
            files.delete_purge,
        )
        self.presigned_post = async_to_raw_response_wrapper(
            files.presigned_post,
        )
        self.retrieve_download = async_to_raw_response_wrapper(
            files.retrieve_download,
        )

    @cached_property
    def multipart(self) -> AsyncMultipartResourceWithRawResponse:
        return AsyncMultipartResourceWithRawResponse(self._files.multipart)


class FilesResourceWithStreamingResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.create = to_streamed_response_wrapper(
            files.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            files.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            files.update,
        )
        self.list = to_streamed_response_wrapper(
            files.list,
        )
        self.delete = to_streamed_response_wrapper(
            files.delete,
        )
        self.delete_purge = to_streamed_response_wrapper(
            files.delete_purge,
        )
        self.presigned_post = to_streamed_response_wrapper(
            files.presigned_post,
        )
        self.retrieve_download = to_streamed_response_wrapper(
            files.retrieve_download,
        )

    @cached_property
    def multipart(self) -> MultipartResourceWithStreamingResponse:
        return MultipartResourceWithStreamingResponse(self._files.multipart)


class AsyncFilesResourceWithStreamingResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.create = async_to_streamed_response_wrapper(
            files.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            files.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            files.update,
        )
        self.list = async_to_streamed_response_wrapper(
            files.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            files.delete,
        )
        self.delete_purge = async_to_streamed_response_wrapper(
            files.delete_purge,
        )
        self.presigned_post = async_to_streamed_response_wrapper(
            files.presigned_post,
        )
        self.retrieve_download = async_to_streamed_response_wrapper(
            files.retrieve_download,
        )

    @cached_property
    def multipart(self) -> AsyncMultipartResourceWithStreamingResponse:
        return AsyncMultipartResourceWithStreamingResponse(self._files.multipart)
