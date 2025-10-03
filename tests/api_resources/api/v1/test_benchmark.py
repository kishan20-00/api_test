# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from api_test import APITest, AsyncAPITest
from tests.utils import assert_matches_type
from api_test.types.api.v1 import BenchmarkRetrieveVllmMetricsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBenchmark:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_vllm_metrics(self, client: APITest) -> None:
        benchmark = client.api.v1.benchmark.retrieve_vllm_metrics()
        assert_matches_type(BenchmarkRetrieveVllmMetricsResponse, benchmark, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_vllm_metrics(self, client: APITest) -> None:
        response = client.api.v1.benchmark.with_raw_response.retrieve_vllm_metrics()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benchmark = response.parse()
        assert_matches_type(BenchmarkRetrieveVllmMetricsResponse, benchmark, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_vllm_metrics(self, client: APITest) -> None:
        with client.api.v1.benchmark.with_streaming_response.retrieve_vllm_metrics() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benchmark = response.parse()
            assert_matches_type(BenchmarkRetrieveVllmMetricsResponse, benchmark, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBenchmark:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_vllm_metrics(self, async_client: AsyncAPITest) -> None:
        benchmark = await async_client.api.v1.benchmark.retrieve_vllm_metrics()
        assert_matches_type(BenchmarkRetrieveVllmMetricsResponse, benchmark, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_vllm_metrics(self, async_client: AsyncAPITest) -> None:
        response = await async_client.api.v1.benchmark.with_raw_response.retrieve_vllm_metrics()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benchmark = await response.parse()
        assert_matches_type(BenchmarkRetrieveVllmMetricsResponse, benchmark, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_vllm_metrics(self, async_client: AsyncAPITest) -> None:
        async with async_client.api.v1.benchmark.with_streaming_response.retrieve_vllm_metrics() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benchmark = await response.parse()
            assert_matches_type(BenchmarkRetrieveVllmMetricsResponse, benchmark, path=["response"])

        assert cast(Any, response.is_closed) is True
