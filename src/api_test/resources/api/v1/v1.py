# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, Iterable, Optional, cast

import httpx

from .keys import (
    KeysResource,
    AsyncKeysResource,
    KeysResourceWithRawResponse,
    AsyncKeysResourceWithRawResponse,
    KeysResourceWithStreamingResponse,
    AsyncKeysResourceWithStreamingResponse,
)
from .logs import (
    LogsResource,
    AsyncLogsResource,
    LogsResourceWithRawResponse,
    AsyncLogsResourceWithRawResponse,
    LogsResourceWithStreamingResponse,
    AsyncLogsResourceWithStreamingResponse,
)
from .debug import (
    DebugResource,
    AsyncDebugResource,
    DebugResourceWithRawResponse,
    AsyncDebugResourceWithRawResponse,
    DebugResourceWithStreamingResponse,
    AsyncDebugResourceWithStreamingResponse,
)
from .users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)
from .storage import (
    StorageResource,
    AsyncStorageResource,
    StorageResourceWithRawResponse,
    AsyncStorageResourceWithRawResponse,
    StorageResourceWithStreamingResponse,
    AsyncStorageResourceWithStreamingResponse,
)
from .messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from ...._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from ...._compat import cached_property
from .files.files import (
    FilesResource,
    AsyncFilesResource,
    FilesResourceWithRawResponse,
    AsyncFilesResourceWithRawResponse,
    FilesResourceWithStreamingResponse,
    AsyncFilesResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.api import (
    v1_generate_params,
    v1_save_message_params,
    v1_generate_image_params,
    v1_audio_inference_params,
    v1_retrieve_api_key_logs_params,
)
from .conversations import (
    ConversationsResource,
    AsyncConversationsResource,
    ConversationsResourceWithRawResponse,
    AsyncConversationsResourceWithRawResponse,
    ConversationsResourceWithStreamingResponse,
    AsyncConversationsResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from .benchmark.benchmark import (
    BenchmarkResource,
    AsyncBenchmarkResource,
    BenchmarkResourceWithRawResponse,
    AsyncBenchmarkResourceWithRawResponse,
    BenchmarkResourceWithStreamingResponse,
    AsyncBenchmarkResourceWithStreamingResponse,
)
from ....types.api.v1_audio_inference_response import V1AudioInferenceResponse

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def debug(self) -> DebugResource:
        return DebugResource(self._client)

    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def conversations(self) -> ConversationsResource:
        return ConversationsResource(self._client)

    @cached_property
    def messages(self) -> MessagesResource:
        return MessagesResource(self._client)

    @cached_property
    def logs(self) -> LogsResource:
        return LogsResource(self._client)

    @cached_property
    def benchmark(self) -> BenchmarkResource:
        return BenchmarkResource(self._client)

    @cached_property
    def keys(self) -> KeysResource:
        return KeysResource(self._client)

    @cached_property
    def storage(self) -> StorageResource:
        return StorageResource(self._client)

    @cached_property
    def files(self) -> FilesResource:
        return FilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)

    def audio_inference(
        self,
        *,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1AudioInferenceResponse:
        """
        Handles audio file upload for speech-to-text inference, performing necessary
        conversion (e.g., to 16kHz mono WAV) before sending to the LLM backend.

        Args: request: The FastAPI Request object. file: The uploaded audio file.
        current_user: The authenticated user object or None. log_model: Dependency for
        creating log entries.

        Returns: AudioInferenceResponse: The transcription result including text,
        duration, and language.

        Raises: HTTPException: 400 If the file format is unsupported or audio conversion
        fails. HTTPException: 500 For LLM API or internal processing errors.

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
            "/api/v1/audio-inference",
            body=maybe_transform(body, v1_audio_inference_params.V1AudioInferenceParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1AudioInferenceResponse,
        )

    def generate(
        self,
        *,
        messages: Iterable[v1_generate_params.Message],
        max_tokens: int | Omit = omit,
        model: str | Omit = omit,
        seed: Optional[int] | Omit = omit,
        stop_sequence: Optional[str] | Omit = omit,
        stream: bool | Omit = omit,
        temperature: float | Omit = omit,
        top_k: int | Omit = omit,
        top_p: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Handles LLM text completion and chat requests, supporting both standard and
        streaming responses. Logs the interaction details regardless of success or
        failure.

        Args: fastapi_request: The FastAPI Request object. request_data: The Pydantic
        model containing the chat/completion parameters. current_user: The authenticated
        user object or None. log_model: Dependency for creating log entries.

        Returns: Union[Dict[str, Any], StreamingResponse]: The JSON response or a
        Server-Sent Events (SSE) stream.

        Raises: HTTPException: 501 If the LLM client is not configured for the model.
        HTTPException: 500/400 For LLM API interaction errors.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/generate",
            body=maybe_transform(
                {
                    "messages": messages,
                    "max_tokens": max_tokens,
                    "model": model,
                    "seed": seed,
                    "stop_sequence": stop_sequence,
                    "stream": stream,
                    "temperature": temperature,
                    "top_k": top_k,
                    "top_p": top_p,
                },
                v1_generate_params.V1GenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def generate_image(
        self,
        *,
        model: str,
        prompt: str,
        guidance_scale: Optional[float] | Omit = omit,
        negative_prompt: Optional[str] | Omit = omit,
        num_inference_steps: Optional[int] | Omit = omit,
        poll_interval: Optional[float] | Omit = omit,
        seed: Optional[int] | Omit = omit,
        api_timeout: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Handles requests for image generation, supporting two distinct model approaches:

        1. Polling-based (e.g., sdm-3.5) with timeout.
        2. Direct generation (e.g., sdxl) returning the image bytes immediately. The
           final image is streamed back as a PNG.

        Args: request_data: The Pydantic model containing the prompt, model, and
        generation parameters. current_user: The authenticated user object or None.
        log_model: Dependency for creating log entries.

        Returns: StreamingResponse: The generated image file streamed as 'image/png'.

        Raises: HTTPException: 400 If the model is unsupported or invalid.
        HTTPException: 501 If the LLM client configuration is incomplete. HTTPException:
        504 If a polling task times out. HTTPException: 500/4xx For internal/API errors
        during generation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/generate-image",
            body=maybe_transform(
                {
                    "model": model,
                    "prompt": prompt,
                    "guidance_scale": guidance_scale,
                    "negative_prompt": negative_prompt,
                    "num_inference_steps": num_inference_steps,
                    "poll_interval": poll_interval,
                    "seed": seed,
                    "api_timeout": api_timeout,
                },
                v1_generate_image_params.V1GenerateImageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def retrieve_api_key_logs(
        self,
        *,
        end_time: int | Omit = omit,
        only_errors: bool | Omit = omit,
        page_num: int | Omit = omit,
        page_size: int | Omit = omit,
        start_time: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Retrieves a paginated and filterable list of API key usage logs for the current
        authenticated user.

        Args: current_user: The authenticated user obtained via dependency.
        key_log_model: Dependency providing access to the API key log database model.
        only_errors: Query parameter to filter for error logs only. start_time: Query
        parameter specifying the start of the time range (Unix ms). end_time: Query
        parameter specifying the end of the time range (Unix ms). page_num: Query
        parameter for the requested page number. page_size: Query parameter for the
        number of items per page.

        Returns: dict: A dictionary containing the list of logs and total count.

        Raises: HTTPException: 401 If the user is unauthenticated.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/api-key-logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_time": end_time,
                        "only_errors": only_errors,
                        "page_num": page_num,
                        "page_size": page_size,
                        "start_time": start_time,
                    },
                    v1_retrieve_api_key_logs_params.V1RetrieveAPIKeyLogsParams,
                ),
            ),
            cast_to=object,
        )

    def retrieve_health(
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
        Performs a basic health check on the API service.

        Args: None

        Returns: dict: A dictionary containing the status and current UTC timestamp.

        Raises: None
        """
        return self._get(
            "/api/v1/health",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def retrieve_token_count(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Placeholder endpoint for future token usage accounting logic.

        Returns status
        information about token counting for the current user.

        Args: current_user: The authenticated user object or None.

        Returns: dict: Status information regarding token count retrieval.

        Raises: None
        """
        return self._get(
            "/api/v1/token-count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def save_message(
        self,
        *,
        is_stream: bool,
        latency: str,
        model_id: str,
        prompt: str,
        response: str,
        token_count: int,
        token_persecond: float,
        conversation_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Saves a user prompt and model response as a message pair in the database.

        If no
        conversation ID is provided, it creates a new conversation first.

        Args: request_data: The message data including prompt, response, metrics, and
        conversation ID. current_user: The authenticated user object. conv_model:
        Dependency for conversation DB operations. msg_model: Dependency for message DB
        operations. log_model: Dependency for creating log entries.

        Returns: dict: Confirmation of the save operation including conversation and
        message IDs.

        Raises: HTTPException: 401 If the user is unauthenticated. HTTPException: 400 If
        the provided conversation ID is invalid. HTTPException: 500 For database errors
        during save or creation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/save-message",
            body=maybe_transform(
                {
                    "is_stream": is_stream,
                    "latency": latency,
                    "model_id": model_id,
                    "prompt": prompt,
                    "response": response,
                    "token_count": token_count,
                    "token_persecond": token_persecond,
                    "conversation_id": conversation_id,
                },
                v1_save_message_params.V1SaveMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def debug(self) -> AsyncDebugResource:
        return AsyncDebugResource(self._client)

    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def conversations(self) -> AsyncConversationsResource:
        return AsyncConversationsResource(self._client)

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        return AsyncMessagesResource(self._client)

    @cached_property
    def logs(self) -> AsyncLogsResource:
        return AsyncLogsResource(self._client)

    @cached_property
    def benchmark(self) -> AsyncBenchmarkResource:
        return AsyncBenchmarkResource(self._client)

    @cached_property
    def keys(self) -> AsyncKeysResource:
        return AsyncKeysResource(self._client)

    @cached_property
    def storage(self) -> AsyncStorageResource:
        return AsyncStorageResource(self._client)

    @cached_property
    def files(self) -> AsyncFilesResource:
        return AsyncFilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/api_test-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)

    async def audio_inference(
        self,
        *,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1AudioInferenceResponse:
        """
        Handles audio file upload for speech-to-text inference, performing necessary
        conversion (e.g., to 16kHz mono WAV) before sending to the LLM backend.

        Args: request: The FastAPI Request object. file: The uploaded audio file.
        current_user: The authenticated user object or None. log_model: Dependency for
        creating log entries.

        Returns: AudioInferenceResponse: The transcription result including text,
        duration, and language.

        Raises: HTTPException: 400 If the file format is unsupported or audio conversion
        fails. HTTPException: 500 For LLM API or internal processing errors.

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
            "/api/v1/audio-inference",
            body=await async_maybe_transform(body, v1_audio_inference_params.V1AudioInferenceParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1AudioInferenceResponse,
        )

    async def generate(
        self,
        *,
        messages: Iterable[v1_generate_params.Message],
        max_tokens: int | Omit = omit,
        model: str | Omit = omit,
        seed: Optional[int] | Omit = omit,
        stop_sequence: Optional[str] | Omit = omit,
        stream: bool | Omit = omit,
        temperature: float | Omit = omit,
        top_k: int | Omit = omit,
        top_p: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Handles LLM text completion and chat requests, supporting both standard and
        streaming responses. Logs the interaction details regardless of success or
        failure.

        Args: fastapi_request: The FastAPI Request object. request_data: The Pydantic
        model containing the chat/completion parameters. current_user: The authenticated
        user object or None. log_model: Dependency for creating log entries.

        Returns: Union[Dict[str, Any], StreamingResponse]: The JSON response or a
        Server-Sent Events (SSE) stream.

        Raises: HTTPException: 501 If the LLM client is not configured for the model.
        HTTPException: 500/400 For LLM API interaction errors.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/generate",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "max_tokens": max_tokens,
                    "model": model,
                    "seed": seed,
                    "stop_sequence": stop_sequence,
                    "stream": stream,
                    "temperature": temperature,
                    "top_k": top_k,
                    "top_p": top_p,
                },
                v1_generate_params.V1GenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def generate_image(
        self,
        *,
        model: str,
        prompt: str,
        guidance_scale: Optional[float] | Omit = omit,
        negative_prompt: Optional[str] | Omit = omit,
        num_inference_steps: Optional[int] | Omit = omit,
        poll_interval: Optional[float] | Omit = omit,
        seed: Optional[int] | Omit = omit,
        api_timeout: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Handles requests for image generation, supporting two distinct model approaches:

        1. Polling-based (e.g., sdm-3.5) with timeout.
        2. Direct generation (e.g., sdxl) returning the image bytes immediately. The
           final image is streamed back as a PNG.

        Args: request_data: The Pydantic model containing the prompt, model, and
        generation parameters. current_user: The authenticated user object or None.
        log_model: Dependency for creating log entries.

        Returns: StreamingResponse: The generated image file streamed as 'image/png'.

        Raises: HTTPException: 400 If the model is unsupported or invalid.
        HTTPException: 501 If the LLM client configuration is incomplete. HTTPException:
        504 If a polling task times out. HTTPException: 500/4xx For internal/API errors
        during generation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/generate-image",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "prompt": prompt,
                    "guidance_scale": guidance_scale,
                    "negative_prompt": negative_prompt,
                    "num_inference_steps": num_inference_steps,
                    "poll_interval": poll_interval,
                    "seed": seed,
                    "api_timeout": api_timeout,
                },
                v1_generate_image_params.V1GenerateImageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def retrieve_api_key_logs(
        self,
        *,
        end_time: int | Omit = omit,
        only_errors: bool | Omit = omit,
        page_num: int | Omit = omit,
        page_size: int | Omit = omit,
        start_time: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Retrieves a paginated and filterable list of API key usage logs for the current
        authenticated user.

        Args: current_user: The authenticated user obtained via dependency.
        key_log_model: Dependency providing access to the API key log database model.
        only_errors: Query parameter to filter for error logs only. start_time: Query
        parameter specifying the start of the time range (Unix ms). end_time: Query
        parameter specifying the end of the time range (Unix ms). page_num: Query
        parameter for the requested page number. page_size: Query parameter for the
        number of items per page.

        Returns: dict: A dictionary containing the list of logs and total count.

        Raises: HTTPException: 401 If the user is unauthenticated.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/api-key-logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_time": end_time,
                        "only_errors": only_errors,
                        "page_num": page_num,
                        "page_size": page_size,
                        "start_time": start_time,
                    },
                    v1_retrieve_api_key_logs_params.V1RetrieveAPIKeyLogsParams,
                ),
            ),
            cast_to=object,
        )

    async def retrieve_health(
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
        Performs a basic health check on the API service.

        Args: None

        Returns: dict: A dictionary containing the status and current UTC timestamp.

        Raises: None
        """
        return await self._get(
            "/api/v1/health",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def retrieve_token_count(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Placeholder endpoint for future token usage accounting logic.

        Returns status
        information about token counting for the current user.

        Args: current_user: The authenticated user object or None.

        Returns: dict: Status information regarding token count retrieval.

        Raises: None
        """
        return await self._get(
            "/api/v1/token-count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def save_message(
        self,
        *,
        is_stream: bool,
        latency: str,
        model_id: str,
        prompt: str,
        response: str,
        token_count: int,
        token_persecond: float,
        conversation_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Saves a user prompt and model response as a message pair in the database.

        If no
        conversation ID is provided, it creates a new conversation first.

        Args: request_data: The message data including prompt, response, metrics, and
        conversation ID. current_user: The authenticated user object. conv_model:
        Dependency for conversation DB operations. msg_model: Dependency for message DB
        operations. log_model: Dependency for creating log entries.

        Returns: dict: Confirmation of the save operation including conversation and
        message IDs.

        Raises: HTTPException: 401 If the user is unauthenticated. HTTPException: 400 If
        the provided conversation ID is invalid. HTTPException: 500 For database errors
        during save or creation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/save-message",
            body=await async_maybe_transform(
                {
                    "is_stream": is_stream,
                    "latency": latency,
                    "model_id": model_id,
                    "prompt": prompt,
                    "response": response,
                    "token_count": token_count,
                    "token_persecond": token_persecond,
                    "conversation_id": conversation_id,
                },
                v1_save_message_params.V1SaveMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.audio_inference = to_raw_response_wrapper(
            v1.audio_inference,
        )
        self.generate = to_raw_response_wrapper(
            v1.generate,
        )
        self.generate_image = to_raw_response_wrapper(
            v1.generate_image,
        )
        self.retrieve_api_key_logs = to_raw_response_wrapper(
            v1.retrieve_api_key_logs,
        )
        self.retrieve_health = to_raw_response_wrapper(
            v1.retrieve_health,
        )
        self.retrieve_token_count = to_raw_response_wrapper(
            v1.retrieve_token_count,
        )
        self.save_message = to_raw_response_wrapper(
            v1.save_message,
        )

    @cached_property
    def debug(self) -> DebugResourceWithRawResponse:
        return DebugResourceWithRawResponse(self._v1.debug)

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._v1.users)

    @cached_property
    def conversations(self) -> ConversationsResourceWithRawResponse:
        return ConversationsResourceWithRawResponse(self._v1.conversations)

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        return MessagesResourceWithRawResponse(self._v1.messages)

    @cached_property
    def logs(self) -> LogsResourceWithRawResponse:
        return LogsResourceWithRawResponse(self._v1.logs)

    @cached_property
    def benchmark(self) -> BenchmarkResourceWithRawResponse:
        return BenchmarkResourceWithRawResponse(self._v1.benchmark)

    @cached_property
    def keys(self) -> KeysResourceWithRawResponse:
        return KeysResourceWithRawResponse(self._v1.keys)

    @cached_property
    def storage(self) -> StorageResourceWithRawResponse:
        return StorageResourceWithRawResponse(self._v1.storage)

    @cached_property
    def files(self) -> FilesResourceWithRawResponse:
        return FilesResourceWithRawResponse(self._v1.files)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.audio_inference = async_to_raw_response_wrapper(
            v1.audio_inference,
        )
        self.generate = async_to_raw_response_wrapper(
            v1.generate,
        )
        self.generate_image = async_to_raw_response_wrapper(
            v1.generate_image,
        )
        self.retrieve_api_key_logs = async_to_raw_response_wrapper(
            v1.retrieve_api_key_logs,
        )
        self.retrieve_health = async_to_raw_response_wrapper(
            v1.retrieve_health,
        )
        self.retrieve_token_count = async_to_raw_response_wrapper(
            v1.retrieve_token_count,
        )
        self.save_message = async_to_raw_response_wrapper(
            v1.save_message,
        )

    @cached_property
    def debug(self) -> AsyncDebugResourceWithRawResponse:
        return AsyncDebugResourceWithRawResponse(self._v1.debug)

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._v1.users)

    @cached_property
    def conversations(self) -> AsyncConversationsResourceWithRawResponse:
        return AsyncConversationsResourceWithRawResponse(self._v1.conversations)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        return AsyncMessagesResourceWithRawResponse(self._v1.messages)

    @cached_property
    def logs(self) -> AsyncLogsResourceWithRawResponse:
        return AsyncLogsResourceWithRawResponse(self._v1.logs)

    @cached_property
    def benchmark(self) -> AsyncBenchmarkResourceWithRawResponse:
        return AsyncBenchmarkResourceWithRawResponse(self._v1.benchmark)

    @cached_property
    def keys(self) -> AsyncKeysResourceWithRawResponse:
        return AsyncKeysResourceWithRawResponse(self._v1.keys)

    @cached_property
    def storage(self) -> AsyncStorageResourceWithRawResponse:
        return AsyncStorageResourceWithRawResponse(self._v1.storage)

    @cached_property
    def files(self) -> AsyncFilesResourceWithRawResponse:
        return AsyncFilesResourceWithRawResponse(self._v1.files)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.audio_inference = to_streamed_response_wrapper(
            v1.audio_inference,
        )
        self.generate = to_streamed_response_wrapper(
            v1.generate,
        )
        self.generate_image = to_streamed_response_wrapper(
            v1.generate_image,
        )
        self.retrieve_api_key_logs = to_streamed_response_wrapper(
            v1.retrieve_api_key_logs,
        )
        self.retrieve_health = to_streamed_response_wrapper(
            v1.retrieve_health,
        )
        self.retrieve_token_count = to_streamed_response_wrapper(
            v1.retrieve_token_count,
        )
        self.save_message = to_streamed_response_wrapper(
            v1.save_message,
        )

    @cached_property
    def debug(self) -> DebugResourceWithStreamingResponse:
        return DebugResourceWithStreamingResponse(self._v1.debug)

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._v1.users)

    @cached_property
    def conversations(self) -> ConversationsResourceWithStreamingResponse:
        return ConversationsResourceWithStreamingResponse(self._v1.conversations)

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        return MessagesResourceWithStreamingResponse(self._v1.messages)

    @cached_property
    def logs(self) -> LogsResourceWithStreamingResponse:
        return LogsResourceWithStreamingResponse(self._v1.logs)

    @cached_property
    def benchmark(self) -> BenchmarkResourceWithStreamingResponse:
        return BenchmarkResourceWithStreamingResponse(self._v1.benchmark)

    @cached_property
    def keys(self) -> KeysResourceWithStreamingResponse:
        return KeysResourceWithStreamingResponse(self._v1.keys)

    @cached_property
    def storage(self) -> StorageResourceWithStreamingResponse:
        return StorageResourceWithStreamingResponse(self._v1.storage)

    @cached_property
    def files(self) -> FilesResourceWithStreamingResponse:
        return FilesResourceWithStreamingResponse(self._v1.files)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.audio_inference = async_to_streamed_response_wrapper(
            v1.audio_inference,
        )
        self.generate = async_to_streamed_response_wrapper(
            v1.generate,
        )
        self.generate_image = async_to_streamed_response_wrapper(
            v1.generate_image,
        )
        self.retrieve_api_key_logs = async_to_streamed_response_wrapper(
            v1.retrieve_api_key_logs,
        )
        self.retrieve_health = async_to_streamed_response_wrapper(
            v1.retrieve_health,
        )
        self.retrieve_token_count = async_to_streamed_response_wrapper(
            v1.retrieve_token_count,
        )
        self.save_message = async_to_streamed_response_wrapper(
            v1.save_message,
        )

    @cached_property
    def debug(self) -> AsyncDebugResourceWithStreamingResponse:
        return AsyncDebugResourceWithStreamingResponse(self._v1.debug)

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._v1.users)

    @cached_property
    def conversations(self) -> AsyncConversationsResourceWithStreamingResponse:
        return AsyncConversationsResourceWithStreamingResponse(self._v1.conversations)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._v1.messages)

    @cached_property
    def logs(self) -> AsyncLogsResourceWithStreamingResponse:
        return AsyncLogsResourceWithStreamingResponse(self._v1.logs)

    @cached_property
    def benchmark(self) -> AsyncBenchmarkResourceWithStreamingResponse:
        return AsyncBenchmarkResourceWithStreamingResponse(self._v1.benchmark)

    @cached_property
    def keys(self) -> AsyncKeysResourceWithStreamingResponse:
        return AsyncKeysResourceWithStreamingResponse(self._v1.keys)

    @cached_property
    def storage(self) -> AsyncStorageResourceWithStreamingResponse:
        return AsyncStorageResourceWithStreamingResponse(self._v1.storage)

    @cached_property
    def files(self) -> AsyncFilesResourceWithStreamingResponse:
        return AsyncFilesResourceWithStreamingResponse(self._v1.files)
