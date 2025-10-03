# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from api_test import APITest, AsyncAPITest
from tests.utils import assert_matches_type
from api_test.types.api.v1 import User

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDebug:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_current_user(self, client: APITest) -> None:
        debug = client.api.v1.debug.retrieve_current_user()
        assert_matches_type(User, debug, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_current_user(self, client: APITest) -> None:
        response = client.api.v1.debug.with_raw_response.retrieve_current_user()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        debug = response.parse()
        assert_matches_type(User, debug, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_current_user(self, client: APITest) -> None:
        with client.api.v1.debug.with_streaming_response.retrieve_current_user() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            debug = response.parse()
            assert_matches_type(User, debug, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDebug:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_current_user(self, async_client: AsyncAPITest) -> None:
        debug = await async_client.api.v1.debug.retrieve_current_user()
        assert_matches_type(User, debug, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_current_user(self, async_client: AsyncAPITest) -> None:
        response = await async_client.api.v1.debug.with_raw_response.retrieve_current_user()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        debug = await response.parse()
        assert_matches_type(User, debug, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_current_user(self, async_client: AsyncAPITest) -> None:
        async with async_client.api.v1.debug.with_streaming_response.retrieve_current_user() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            debug = await response.parse()
            assert_matches_type(User, debug, path=["response"])

        assert cast(Any, response.is_closed) is True
