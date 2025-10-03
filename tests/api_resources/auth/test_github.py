# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from api_test import APITest, AsyncAPITest
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGitHub:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_callback(self, client: APITest) -> None:
        github = client.auth.github.callback()
        assert_matches_type(object, github, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_callback(self, client: APITest) -> None:
        response = client.auth.github.with_raw_response.callback()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = response.parse()
        assert_matches_type(object, github, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_callback(self, client: APITest) -> None:
        with client.auth.github.with_streaming_response.callback() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = response.parse()
            assert_matches_type(object, github, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGitHub:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_callback(self, async_client: AsyncAPITest) -> None:
        github = await async_client.auth.github.callback()
        assert_matches_type(object, github, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_callback(self, async_client: AsyncAPITest) -> None:
        response = await async_client.auth.github.with_raw_response.callback()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = await response.parse()
        assert_matches_type(object, github, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_callback(self, async_client: AsyncAPITest) -> None:
        async with async_client.auth.github.with_streaming_response.callback() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = await response.parse()
            assert_matches_type(object, github, path=["response"])

        assert cast(Any, response.is_closed) is True
