# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from api_test import APITest, AsyncAPITest
from tests.utils import assert_matches_type
from api_test.types.api.v1 import Conversation

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConversations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: APITest) -> None:
        conversation = client.api.v1.conversations.retrieve(
            "user_id",
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: APITest) -> None:
        response = client.api.v1.conversations.with_raw_response.retrieve(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(Conversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: APITest) -> None:
        with client.api.v1.conversations.with_streaming_response.retrieve(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(Conversation, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: APITest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.api.v1.conversations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: APITest) -> None:
        conversation = client.api.v1.conversations.update(
            conv_id="conv_id",
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: APITest) -> None:
        conversation = client.api.v1.conversations.update(
            conv_id="conv_id",
            title="Updated Conversation Title",
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: APITest) -> None:
        response = client.api.v1.conversations.with_raw_response.update(
            conv_id="conv_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(Conversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: APITest) -> None:
        with client.api.v1.conversations.with_streaming_response.update(
            conv_id="conv_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(Conversation, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: APITest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conv_id` but received ''"):
            client.api.v1.conversations.with_raw_response.update(
                conv_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: APITest) -> None:
        conversation = client.api.v1.conversations.delete(
            "conv_id",
        )
        assert conversation is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: APITest) -> None:
        response = client.api.v1.conversations.with_raw_response.delete(
            "conv_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert conversation is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: APITest) -> None:
        with client.api.v1.conversations.with_streaming_response.delete(
            "conv_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert conversation is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: APITest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conv_id` but received ''"):
            client.api.v1.conversations.with_raw_response.delete(
                "",
            )


class TestAsyncConversations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAPITest) -> None:
        conversation = await async_client.api.v1.conversations.retrieve(
            "user_id",
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAPITest) -> None:
        response = await async_client.api.v1.conversations.with_raw_response.retrieve(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(Conversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAPITest) -> None:
        async with async_client.api.v1.conversations.with_streaming_response.retrieve(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(Conversation, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAPITest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.api.v1.conversations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncAPITest) -> None:
        conversation = await async_client.api.v1.conversations.update(
            conv_id="conv_id",
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncAPITest) -> None:
        conversation = await async_client.api.v1.conversations.update(
            conv_id="conv_id",
            title="Updated Conversation Title",
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAPITest) -> None:
        response = await async_client.api.v1.conversations.with_raw_response.update(
            conv_id="conv_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(Conversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAPITest) -> None:
        async with async_client.api.v1.conversations.with_streaming_response.update(
            conv_id="conv_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(Conversation, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncAPITest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conv_id` but received ''"):
            await async_client.api.v1.conversations.with_raw_response.update(
                conv_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncAPITest) -> None:
        conversation = await async_client.api.v1.conversations.delete(
            "conv_id",
        )
        assert conversation is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAPITest) -> None:
        response = await async_client.api.v1.conversations.with_raw_response.delete(
            "conv_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert conversation is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAPITest) -> None:
        async with async_client.api.v1.conversations.with_streaming_response.delete(
            "conv_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert conversation is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAPITest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conv_id` but received ''"):
            await async_client.api.v1.conversations.with_raw_response.delete(
                "",
            )
