# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from api_test import APITest, AsyncAPITest
from tests.utils import assert_matches_type
from api_test.types.api.v1 import Log, LogRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: APITest) -> None:
        log = client.api.v1.logs.retrieve(
            endpoint="endpoint",
        )
        assert_matches_type(LogRetrieveResponse, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: APITest) -> None:
        log = client.api.v1.logs.retrieve(
            endpoint="endpoint",
            limit=1,
            skip=0,
        )
        assert_matches_type(LogRetrieveResponse, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: APITest) -> None:
        response = client.api.v1.logs.with_raw_response.retrieve(
            endpoint="endpoint",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert_matches_type(LogRetrieveResponse, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: APITest) -> None:
        with client.api.v1.logs.with_streaming_response.retrieve(
            endpoint="endpoint",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert_matches_type(LogRetrieveResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: APITest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `endpoint` but received ''"):
            client.api.v1.logs.with_raw_response.retrieve(
                endpoint="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: APITest) -> None:
        log = client.api.v1.logs.update(
            endpoint="x",
            request={"foo": "bar"},
            response={"foo": "bar"},
            status_code=100,
        )
        assert_matches_type(Log, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: APITest) -> None:
        log = client.api.v1.logs.update(
            endpoint="x",
            request={"foo": "bar"},
            response={"foo": "bar"},
            status_code=100,
            user_id="user_id",
        )
        assert_matches_type(Log, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: APITest) -> None:
        response = client.api.v1.logs.with_raw_response.update(
            endpoint="x",
            request={"foo": "bar"},
            response={"foo": "bar"},
            status_code=100,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert_matches_type(Log, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: APITest) -> None:
        with client.api.v1.logs.with_streaming_response.update(
            endpoint="x",
            request={"foo": "bar"},
            response={"foo": "bar"},
            status_code=100,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert_matches_type(Log, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: APITest) -> None:
        log = client.api.v1.logs.retrieve()
        assert_matches_type(LogRetrieveResponse, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: APITest) -> None:
        log = client.api.v1.logs.retrieve(
            limit=1,
            skip=0,
        )
        assert_matches_type(LogRetrieveResponse, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: APITest) -> None:
        response = client.api.v1.logs.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert_matches_type(LogRetrieveResponse, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: APITest) -> None:
        with client.api.v1.logs.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert_matches_type(LogRetrieveResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLogs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAPITest) -> None:
        log = await async_client.api.v1.logs.retrieve(
            endpoint="endpoint",
        )
        assert_matches_type(LogRetrieveResponse, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncAPITest) -> None:
        log = await async_client.api.v1.logs.retrieve(
            endpoint="endpoint",
            limit=1,
            skip=0,
        )
        assert_matches_type(LogRetrieveResponse, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAPITest) -> None:
        response = await async_client.api.v1.logs.with_raw_response.retrieve(
            endpoint="endpoint",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert_matches_type(LogRetrieveResponse, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAPITest) -> None:
        async with async_client.api.v1.logs.with_streaming_response.retrieve(
            endpoint="endpoint",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert_matches_type(LogRetrieveResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAPITest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `endpoint` but received ''"):
            await async_client.api.v1.logs.with_raw_response.retrieve(
                endpoint="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncAPITest) -> None:
        log = await async_client.api.v1.logs.update(
            endpoint="x",
            request={"foo": "bar"},
            response={"foo": "bar"},
            status_code=100,
        )
        assert_matches_type(Log, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncAPITest) -> None:
        log = await async_client.api.v1.logs.update(
            endpoint="x",
            request={"foo": "bar"},
            response={"foo": "bar"},
            status_code=100,
            user_id="user_id",
        )
        assert_matches_type(Log, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAPITest) -> None:
        response = await async_client.api.v1.logs.with_raw_response.update(
            endpoint="x",
            request={"foo": "bar"},
            response={"foo": "bar"},
            status_code=100,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert_matches_type(Log, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAPITest) -> None:
        async with async_client.api.v1.logs.with_streaming_response.update(
            endpoint="x",
            request={"foo": "bar"},
            response={"foo": "bar"},
            status_code=100,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert_matches_type(Log, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAPITest) -> None:
        log = await async_client.api.v1.logs.retrieve()
        assert_matches_type(LogRetrieveResponse, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncAPITest) -> None:
        log = await async_client.api.v1.logs.retrieve(
            limit=1,
            skip=0,
        )
        assert_matches_type(LogRetrieveResponse, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAPITest) -> None:
        response = await async_client.api.v1.logs.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert_matches_type(LogRetrieveResponse, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAPITest) -> None:
        async with async_client.api.v1.logs.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert_matches_type(LogRetrieveResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True
