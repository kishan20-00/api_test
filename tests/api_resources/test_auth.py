# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from api_test import APITest, AsyncAPITest
from tests.utils import assert_matches_type
from api_test.types import TokenResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_logout(self, client: APITest) -> None:
        auth = client.auth.logout()
        assert_matches_type(object, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_logout(self, client: APITest) -> None:
        response = client.auth.with_raw_response.logout()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(object, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_logout(self, client: APITest) -> None:
        with client.auth.with_streaming_response.logout() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(object, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_request_magic_link(self, client: APITest) -> None:
        auth = client.auth.request_magic_link(
            body={"foo": "bar"},
        )
        assert_matches_type(object, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_request_magic_link(self, client: APITest) -> None:
        response = client.auth.with_raw_response.request_magic_link(
            body={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(object, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_request_magic_link(self, client: APITest) -> None:
        with client.auth.with_streaming_response.request_magic_link(
            body={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(object, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_verify_magic_link_token(self, client: APITest) -> None:
        auth = client.auth.verify_magic_link_token(
            token="token",
        )
        assert_matches_type(TokenResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_verify_magic_link_token(self, client: APITest) -> None:
        response = client.auth.with_raw_response.verify_magic_link_token(
            token="token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(TokenResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_verify_magic_link_token(self, client: APITest) -> None:
        with client.auth.with_streaming_response.verify_magic_link_token(
            token="token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(TokenResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuth:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_logout(self, async_client: AsyncAPITest) -> None:
        auth = await async_client.auth.logout()
        assert_matches_type(object, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_logout(self, async_client: AsyncAPITest) -> None:
        response = await async_client.auth.with_raw_response.logout()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(object, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_logout(self, async_client: AsyncAPITest) -> None:
        async with async_client.auth.with_streaming_response.logout() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(object, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_request_magic_link(self, async_client: AsyncAPITest) -> None:
        auth = await async_client.auth.request_magic_link(
            body={"foo": "bar"},
        )
        assert_matches_type(object, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_request_magic_link(self, async_client: AsyncAPITest) -> None:
        response = await async_client.auth.with_raw_response.request_magic_link(
            body={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(object, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_request_magic_link(self, async_client: AsyncAPITest) -> None:
        async with async_client.auth.with_streaming_response.request_magic_link(
            body={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(object, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_verify_magic_link_token(self, async_client: AsyncAPITest) -> None:
        auth = await async_client.auth.verify_magic_link_token(
            token="token",
        )
        assert_matches_type(TokenResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_verify_magic_link_token(self, async_client: AsyncAPITest) -> None:
        response = await async_client.auth.with_raw_response.verify_magic_link_token(
            token="token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(TokenResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_verify_magic_link_token(self, async_client: AsyncAPITest) -> None:
        async with async_client.auth.with_streaming_response.verify_magic_link_token(
            token="token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(TokenResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True
