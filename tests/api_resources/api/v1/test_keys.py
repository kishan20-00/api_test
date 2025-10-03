# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from api_test import APITest, AsyncAPITest
from tests.utils import assert_matches_type
from api_test._utils import parse_datetime
from api_test.types.api.v1 import KeyUpdateResponse, KeyRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: APITest) -> None:
        key = client.api.v1.keys.update(
            display_name="x",
        )
        assert_matches_type(KeyUpdateResponse, key, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: APITest) -> None:
        key = client.api.v1.keys.update(
            display_name="x",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(KeyUpdateResponse, key, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: APITest) -> None:
        response = client.api.v1.keys.with_raw_response.update(
            display_name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(KeyUpdateResponse, key, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: APITest) -> None:
        with client.api.v1.keys.with_streaming_response.update(
            display_name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(KeyUpdateResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: APITest) -> None:
        key = client.api.v1.keys.delete(
            "key_id",
        )
        assert key is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: APITest) -> None:
        response = client.api.v1.keys.with_raw_response.delete(
            "key_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert key is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: APITest) -> None:
        with client.api.v1.keys.with_streaming_response.delete(
            "key_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert key is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: APITest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            client.api.v1.keys.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: APITest) -> None:
        key = client.api.v1.keys.retrieve()
        assert_matches_type(KeyRetrieveResponse, key, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: APITest) -> None:
        key = client.api.v1.keys.retrieve(
            active_only=True,
        )
        assert_matches_type(KeyRetrieveResponse, key, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: APITest) -> None:
        response = client.api.v1.keys.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(KeyRetrieveResponse, key, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: APITest) -> None:
        with client.api.v1.keys.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(KeyRetrieveResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncKeys:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncAPITest) -> None:
        key = await async_client.api.v1.keys.update(
            display_name="x",
        )
        assert_matches_type(KeyUpdateResponse, key, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncAPITest) -> None:
        key = await async_client.api.v1.keys.update(
            display_name="x",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(KeyUpdateResponse, key, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAPITest) -> None:
        response = await async_client.api.v1.keys.with_raw_response.update(
            display_name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(KeyUpdateResponse, key, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAPITest) -> None:
        async with async_client.api.v1.keys.with_streaming_response.update(
            display_name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(KeyUpdateResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncAPITest) -> None:
        key = await async_client.api.v1.keys.delete(
            "key_id",
        )
        assert key is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAPITest) -> None:
        response = await async_client.api.v1.keys.with_raw_response.delete(
            "key_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert key is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAPITest) -> None:
        async with async_client.api.v1.keys.with_streaming_response.delete(
            "key_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert key is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAPITest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            await async_client.api.v1.keys.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAPITest) -> None:
        key = await async_client.api.v1.keys.retrieve()
        assert_matches_type(KeyRetrieveResponse, key, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncAPITest) -> None:
        key = await async_client.api.v1.keys.retrieve(
            active_only=True,
        )
        assert_matches_type(KeyRetrieveResponse, key, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAPITest) -> None:
        response = await async_client.api.v1.keys.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(KeyRetrieveResponse, key, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAPITest) -> None:
        async with async_client.api.v1.keys.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(KeyRetrieveResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True
