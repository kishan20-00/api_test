# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from api_test import APITest, AsyncAPITest
from tests.utils import assert_matches_type
from api_test.types.api import (
    V1AudioInferenceResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_audio_inference(self, client: APITest) -> None:
        v1 = client.api.v1.audio_inference(
            file=b"raw file contents",
        )
        assert_matches_type(V1AudioInferenceResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_audio_inference(self, client: APITest) -> None:
        response = client.api.v1.with_raw_response.audio_inference(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1AudioInferenceResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_audio_inference(self, client: APITest) -> None:
        with client.api.v1.with_streaming_response.audio_inference(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1AudioInferenceResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_generate(self, client: APITest) -> None:
        v1 = client.api.v1.generate(
            messages=[{"role": "role"}],
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_generate_with_all_params(self, client: APITest) -> None:
        v1 = client.api.v1.generate(
            messages=[
                {
                    "role": "role",
                    "content": "string",
                    "function_call": {"foo": "bar"},
                    "name": "name",
                    "refusal": "refusal",
                    "tool_call_id": "tool_call_id",
                    "tool_calls": [{"foo": "bar"}],
                }
            ],
            max_tokens=1,
            model="model",
            seed=0,
            stop_sequence="stopSequence",
            stream=True,
            temperature=0,
            top_k=1,
            top_p=0,
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_generate(self, client: APITest) -> None:
        response = client.api.v1.with_raw_response.generate(
            messages=[{"role": "role"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_generate(self, client: APITest) -> None:
        with client.api.v1.with_streaming_response.generate(
            messages=[{"role": "role"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(object, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_generate_image(self, client: APITest) -> None:
        v1 = client.api.v1.generate_image(
            model="model",
            prompt="prompt",
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_generate_image_with_all_params(self, client: APITest) -> None:
        v1 = client.api.v1.generate_image(
            model="model",
            prompt="prompt",
            guidance_scale=0,
            negative_prompt="negative_prompt",
            num_inference_steps=0,
            poll_interval=0,
            seed=0,
            api_timeout=0,
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_generate_image(self, client: APITest) -> None:
        response = client.api.v1.with_raw_response.generate_image(
            model="model",
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_generate_image(self, client: APITest) -> None:
        with client.api.v1.with_streaming_response.generate_image(
            model="model",
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(object, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_api_key_logs(self, client: APITest) -> None:
        v1 = client.api.v1.retrieve_api_key_logs()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_api_key_logs_with_all_params(self, client: APITest) -> None:
        v1 = client.api.v1.retrieve_api_key_logs(
            end_time=0,
            only_errors=True,
            page_num=0,
            page_size=0,
            start_time=0,
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_api_key_logs(self, client: APITest) -> None:
        response = client.api.v1.with_raw_response.retrieve_api_key_logs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_api_key_logs(self, client: APITest) -> None:
        with client.api.v1.with_streaming_response.retrieve_api_key_logs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(object, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_health(self, client: APITest) -> None:
        v1 = client.api.v1.retrieve_health()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_health(self, client: APITest) -> None:
        response = client.api.v1.with_raw_response.retrieve_health()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_health(self, client: APITest) -> None:
        with client.api.v1.with_streaming_response.retrieve_health() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(object, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_token_count(self, client: APITest) -> None:
        v1 = client.api.v1.retrieve_token_count()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_token_count(self, client: APITest) -> None:
        response = client.api.v1.with_raw_response.retrieve_token_count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_token_count(self, client: APITest) -> None:
        with client.api.v1.with_streaming_response.retrieve_token_count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(object, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_save_message(self, client: APITest) -> None:
        v1 = client.api.v1.save_message(
            is_stream=True,
            latency="latency",
            model_id="model_id",
            prompt="prompt",
            response="response",
            token_count=0,
            token_persecond=0,
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_save_message_with_all_params(self, client: APITest) -> None:
        v1 = client.api.v1.save_message(
            is_stream=True,
            latency="latency",
            model_id="model_id",
            prompt="prompt",
            response="response",
            token_count=0,
            token_persecond=0,
            conversation_id="conversation_id",
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_save_message(self, client: APITest) -> None:
        response = client.api.v1.with_raw_response.save_message(
            is_stream=True,
            latency="latency",
            model_id="model_id",
            prompt="prompt",
            response="response",
            token_count=0,
            token_persecond=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_save_message(self, client: APITest) -> None:
        with client.api.v1.with_streaming_response.save_message(
            is_stream=True,
            latency="latency",
            model_id="model_id",
            prompt="prompt",
            response="response",
            token_count=0,
            token_persecond=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(object, v1, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV1:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_audio_inference(self, async_client: AsyncAPITest) -> None:
        v1 = await async_client.api.v1.audio_inference(
            file=b"raw file contents",
        )
        assert_matches_type(V1AudioInferenceResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_audio_inference(self, async_client: AsyncAPITest) -> None:
        response = await async_client.api.v1.with_raw_response.audio_inference(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1AudioInferenceResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_audio_inference(self, async_client: AsyncAPITest) -> None:
        async with async_client.api.v1.with_streaming_response.audio_inference(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1AudioInferenceResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_generate(self, async_client: AsyncAPITest) -> None:
        v1 = await async_client.api.v1.generate(
            messages=[{"role": "role"}],
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_generate_with_all_params(self, async_client: AsyncAPITest) -> None:
        v1 = await async_client.api.v1.generate(
            messages=[
                {
                    "role": "role",
                    "content": "string",
                    "function_call": {"foo": "bar"},
                    "name": "name",
                    "refusal": "refusal",
                    "tool_call_id": "tool_call_id",
                    "tool_calls": [{"foo": "bar"}],
                }
            ],
            max_tokens=1,
            model="model",
            seed=0,
            stop_sequence="stopSequence",
            stream=True,
            temperature=0,
            top_k=1,
            top_p=0,
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_generate(self, async_client: AsyncAPITest) -> None:
        response = await async_client.api.v1.with_raw_response.generate(
            messages=[{"role": "role"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_generate(self, async_client: AsyncAPITest) -> None:
        async with async_client.api.v1.with_streaming_response.generate(
            messages=[{"role": "role"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(object, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_generate_image(self, async_client: AsyncAPITest) -> None:
        v1 = await async_client.api.v1.generate_image(
            model="model",
            prompt="prompt",
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_generate_image_with_all_params(self, async_client: AsyncAPITest) -> None:
        v1 = await async_client.api.v1.generate_image(
            model="model",
            prompt="prompt",
            guidance_scale=0,
            negative_prompt="negative_prompt",
            num_inference_steps=0,
            poll_interval=0,
            seed=0,
            api_timeout=0,
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_generate_image(self, async_client: AsyncAPITest) -> None:
        response = await async_client.api.v1.with_raw_response.generate_image(
            model="model",
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_generate_image(self, async_client: AsyncAPITest) -> None:
        async with async_client.api.v1.with_streaming_response.generate_image(
            model="model",
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(object, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_api_key_logs(self, async_client: AsyncAPITest) -> None:
        v1 = await async_client.api.v1.retrieve_api_key_logs()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_api_key_logs_with_all_params(self, async_client: AsyncAPITest) -> None:
        v1 = await async_client.api.v1.retrieve_api_key_logs(
            end_time=0,
            only_errors=True,
            page_num=0,
            page_size=0,
            start_time=0,
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_api_key_logs(self, async_client: AsyncAPITest) -> None:
        response = await async_client.api.v1.with_raw_response.retrieve_api_key_logs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_api_key_logs(self, async_client: AsyncAPITest) -> None:
        async with async_client.api.v1.with_streaming_response.retrieve_api_key_logs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(object, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_health(self, async_client: AsyncAPITest) -> None:
        v1 = await async_client.api.v1.retrieve_health()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_health(self, async_client: AsyncAPITest) -> None:
        response = await async_client.api.v1.with_raw_response.retrieve_health()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_health(self, async_client: AsyncAPITest) -> None:
        async with async_client.api.v1.with_streaming_response.retrieve_health() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(object, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_token_count(self, async_client: AsyncAPITest) -> None:
        v1 = await async_client.api.v1.retrieve_token_count()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_token_count(self, async_client: AsyncAPITest) -> None:
        response = await async_client.api.v1.with_raw_response.retrieve_token_count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_token_count(self, async_client: AsyncAPITest) -> None:
        async with async_client.api.v1.with_streaming_response.retrieve_token_count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(object, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_save_message(self, async_client: AsyncAPITest) -> None:
        v1 = await async_client.api.v1.save_message(
            is_stream=True,
            latency="latency",
            model_id="model_id",
            prompt="prompt",
            response="response",
            token_count=0,
            token_persecond=0,
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_save_message_with_all_params(self, async_client: AsyncAPITest) -> None:
        v1 = await async_client.api.v1.save_message(
            is_stream=True,
            latency="latency",
            model_id="model_id",
            prompt="prompt",
            response="response",
            token_count=0,
            token_persecond=0,
            conversation_id="conversation_id",
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_save_message(self, async_client: AsyncAPITest) -> None:
        response = await async_client.api.v1.with_raw_response.save_message(
            is_stream=True,
            latency="latency",
            model_id="model_id",
            prompt="prompt",
            response="response",
            token_count=0,
            token_persecond=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_save_message(self, async_client: AsyncAPITest) -> None:
        async with async_client.api.v1.with_streaming_response.save_message(
            is_stream=True,
            latency="latency",
            model_id="model_id",
            prompt="prompt",
            response="response",
            token_count=0,
            token_persecond=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(object, v1, path=["response"])

        assert cast(Any, response.is_closed) is True
