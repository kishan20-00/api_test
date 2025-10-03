# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from api_test import APITest, AsyncAPITest
from tests.utils import assert_matches_type
from api_test._utils import parse_date
from api_test.types.api.v1.benchmark import ExternalListResponse, ExternalBenchmarkRecord

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExternal:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: APITest) -> None:
        external = client.api.v1.benchmark.external.create(
            date_recorded=parse_date("2019-12-27"),
            metric_name="metric_name",
            metric_unit="metric_unit",
            metric_value=0,
            model_name="model_name",
            provider_name="provider_name",
        )
        assert_matches_type(ExternalBenchmarkRecord, external, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: APITest) -> None:
        external = client.api.v1.benchmark.external.create(
            date_recorded=parse_date("2019-12-27"),
            metric_name="metric_name",
            metric_unit="metric_unit",
            metric_value=0,
            model_name="model_name",
            provider_name="provider_name",
            benchmark_source_url="https://example.com",
            hardware_info="hardware_info",
            notes="notes",
        )
        assert_matches_type(ExternalBenchmarkRecord, external, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: APITest) -> None:
        response = client.api.v1.benchmark.external.with_raw_response.create(
            date_recorded=parse_date("2019-12-27"),
            metric_name="metric_name",
            metric_unit="metric_unit",
            metric_value=0,
            model_name="model_name",
            provider_name="provider_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external = response.parse()
        assert_matches_type(ExternalBenchmarkRecord, external, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: APITest) -> None:
        with client.api.v1.benchmark.external.with_streaming_response.create(
            date_recorded=parse_date("2019-12-27"),
            metric_name="metric_name",
            metric_unit="metric_unit",
            metric_value=0,
            model_name="model_name",
            provider_name="provider_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external = response.parse()
            assert_matches_type(ExternalBenchmarkRecord, external, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: APITest) -> None:
        external = client.api.v1.benchmark.external.list()
        assert_matches_type(ExternalListResponse, external, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: APITest) -> None:
        response = client.api.v1.benchmark.external.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external = response.parse()
        assert_matches_type(ExternalListResponse, external, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: APITest) -> None:
        with client.api.v1.benchmark.external.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external = response.parse()
            assert_matches_type(ExternalListResponse, external, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExternal:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncAPITest) -> None:
        external = await async_client.api.v1.benchmark.external.create(
            date_recorded=parse_date("2019-12-27"),
            metric_name="metric_name",
            metric_unit="metric_unit",
            metric_value=0,
            model_name="model_name",
            provider_name="provider_name",
        )
        assert_matches_type(ExternalBenchmarkRecord, external, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAPITest) -> None:
        external = await async_client.api.v1.benchmark.external.create(
            date_recorded=parse_date("2019-12-27"),
            metric_name="metric_name",
            metric_unit="metric_unit",
            metric_value=0,
            model_name="model_name",
            provider_name="provider_name",
            benchmark_source_url="https://example.com",
            hardware_info="hardware_info",
            notes="notes",
        )
        assert_matches_type(ExternalBenchmarkRecord, external, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAPITest) -> None:
        response = await async_client.api.v1.benchmark.external.with_raw_response.create(
            date_recorded=parse_date("2019-12-27"),
            metric_name="metric_name",
            metric_unit="metric_unit",
            metric_value=0,
            model_name="model_name",
            provider_name="provider_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external = await response.parse()
        assert_matches_type(ExternalBenchmarkRecord, external, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAPITest) -> None:
        async with async_client.api.v1.benchmark.external.with_streaming_response.create(
            date_recorded=parse_date("2019-12-27"),
            metric_name="metric_name",
            metric_unit="metric_unit",
            metric_value=0,
            model_name="model_name",
            provider_name="provider_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external = await response.parse()
            assert_matches_type(ExternalBenchmarkRecord, external, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncAPITest) -> None:
        external = await async_client.api.v1.benchmark.external.list()
        assert_matches_type(ExternalListResponse, external, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAPITest) -> None:
        response = await async_client.api.v1.benchmark.external.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external = await response.parse()
        assert_matches_type(ExternalListResponse, external, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAPITest) -> None:
        async with async_client.api.v1.benchmark.external.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external = await response.parse()
            assert_matches_type(ExternalListResponse, external, path=["response"])

        assert cast(Any, response.is_closed) is True
