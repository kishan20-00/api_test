# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from api_test import APITest, AsyncAPITest
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_completion(self, client: APITest) -> None:
        chat = client.openai.v1.chat.create_completion(
            body={"foo": "bar"},
        )
        assert_matches_type(object, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_completion(self, client: APITest) -> None:
        response = client.openai.v1.chat.with_raw_response.create_completion(
            body={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(object, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_completion(self, client: APITest) -> None:
        with client.openai.v1.chat.with_streaming_response.create_completion(
            body={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(object, chat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChat:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_completion(self, async_client: AsyncAPITest) -> None:
        chat = await async_client.openai.v1.chat.create_completion(
            body={"foo": "bar"},
        )
        assert_matches_type(object, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_completion(self, async_client: AsyncAPITest) -> None:
        response = await async_client.openai.v1.chat.with_raw_response.create_completion(
            body={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(object, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_completion(self, async_client: AsyncAPITest) -> None:
        async with async_client.openai.v1.chat.with_streaming_response.create_completion(
            body={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(object, chat, path=["response"])

        assert cast(Any, response.is_closed) is True
