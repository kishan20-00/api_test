# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from api_test import APITest, AsyncAPITest
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLogin:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_github(self, client: APITest) -> None:
        login = client.auth.login.github()
        assert_matches_type(object, login, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_github(self, client: APITest) -> None:
        response = client.auth.login.with_raw_response.github()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        login = response.parse()
        assert_matches_type(object, login, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_github(self, client: APITest) -> None:
        with client.auth.login.with_streaming_response.github() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            login = response.parse()
            assert_matches_type(object, login, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_google(self, client: APITest) -> None:
        login = client.auth.login.google()
        assert_matches_type(object, login, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_google(self, client: APITest) -> None:
        response = client.auth.login.with_raw_response.google()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        login = response.parse()
        assert_matches_type(object, login, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_google(self, client: APITest) -> None:
        with client.auth.login.with_streaming_response.google() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            login = response.parse()
            assert_matches_type(object, login, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLogin:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_github(self, async_client: AsyncAPITest) -> None:
        login = await async_client.auth.login.github()
        assert_matches_type(object, login, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_github(self, async_client: AsyncAPITest) -> None:
        response = await async_client.auth.login.with_raw_response.github()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        login = await response.parse()
        assert_matches_type(object, login, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_github(self, async_client: AsyncAPITest) -> None:
        async with async_client.auth.login.with_streaming_response.github() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            login = await response.parse()
            assert_matches_type(object, login, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_google(self, async_client: AsyncAPITest) -> None:
        login = await async_client.auth.login.google()
        assert_matches_type(object, login, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_google(self, async_client: AsyncAPITest) -> None:
        response = await async_client.auth.login.with_raw_response.google()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        login = await response.parse()
        assert_matches_type(object, login, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_google(self, async_client: AsyncAPITest) -> None:
        async with async_client.auth.login.with_streaming_response.google() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            login = await response.parse()
            assert_matches_type(object, login, path=["response"])

        assert cast(Any, response.is_closed) is True
