# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from api_test import APITest, AsyncAPITest
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMultipart:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_abort(self, client: APITest) -> None:
        multipart = client.api.v1.files.multipart.abort(
            upload_id="upload_id",
        )
        assert_matches_type(object, multipart, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_abort(self, client: APITest) -> None:
        response = client.api.v1.files.multipart.with_raw_response.abort(
            upload_id="upload_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        multipart = response.parse()
        assert_matches_type(object, multipart, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_abort(self, client: APITest) -> None:
        with client.api.v1.files.multipart.with_streaming_response.abort(
            upload_id="upload_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            multipart = response.parse()
            assert_matches_type(object, multipart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_complete(self, client: APITest) -> None:
        multipart = client.api.v1.files.multipart.complete(
            file_name="file_name",
            parts=[{"foo": "bar"}],
            upload_id="upload_id",
        )
        assert_matches_type(object, multipart, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_complete(self, client: APITest) -> None:
        response = client.api.v1.files.multipart.with_raw_response.complete(
            file_name="file_name",
            parts=[{"foo": "bar"}],
            upload_id="upload_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        multipart = response.parse()
        assert_matches_type(object, multipart, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_complete(self, client: APITest) -> None:
        with client.api.v1.files.multipart.with_streaming_response.complete(
            file_name="file_name",
            parts=[{"foo": "bar"}],
            upload_id="upload_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            multipart = response.parse()
            assert_matches_type(object, multipart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_init(self, client: APITest) -> None:
        multipart = client.api.v1.files.multipart.init(
            file=b"raw file contents",
        )
        assert_matches_type(object, multipart, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_init(self, client: APITest) -> None:
        response = client.api.v1.files.multipart.with_raw_response.init(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        multipart = response.parse()
        assert_matches_type(object, multipart, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_init(self, client: APITest) -> None:
        with client.api.v1.files.multipart.with_streaming_response.init(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            multipart = response.parse()
            assert_matches_type(object, multipart, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMultipart:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_abort(self, async_client: AsyncAPITest) -> None:
        multipart = await async_client.api.v1.files.multipart.abort(
            upload_id="upload_id",
        )
        assert_matches_type(object, multipart, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_abort(self, async_client: AsyncAPITest) -> None:
        response = await async_client.api.v1.files.multipart.with_raw_response.abort(
            upload_id="upload_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        multipart = await response.parse()
        assert_matches_type(object, multipart, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_abort(self, async_client: AsyncAPITest) -> None:
        async with async_client.api.v1.files.multipart.with_streaming_response.abort(
            upload_id="upload_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            multipart = await response.parse()
            assert_matches_type(object, multipart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_complete(self, async_client: AsyncAPITest) -> None:
        multipart = await async_client.api.v1.files.multipart.complete(
            file_name="file_name",
            parts=[{"foo": "bar"}],
            upload_id="upload_id",
        )
        assert_matches_type(object, multipart, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_complete(self, async_client: AsyncAPITest) -> None:
        response = await async_client.api.v1.files.multipart.with_raw_response.complete(
            file_name="file_name",
            parts=[{"foo": "bar"}],
            upload_id="upload_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        multipart = await response.parse()
        assert_matches_type(object, multipart, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_complete(self, async_client: AsyncAPITest) -> None:
        async with async_client.api.v1.files.multipart.with_streaming_response.complete(
            file_name="file_name",
            parts=[{"foo": "bar"}],
            upload_id="upload_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            multipart = await response.parse()
            assert_matches_type(object, multipart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_init(self, async_client: AsyncAPITest) -> None:
        multipart = await async_client.api.v1.files.multipart.init(
            file=b"raw file contents",
        )
        assert_matches_type(object, multipart, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_init(self, async_client: AsyncAPITest) -> None:
        response = await async_client.api.v1.files.multipart.with_raw_response.init(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        multipart = await response.parse()
        assert_matches_type(object, multipart, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_init(self, async_client: AsyncAPITest) -> None:
        async with async_client.api.v1.files.multipart.with_streaming_response.init(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            multipart = await response.parse()
            assert_matches_type(object, multipart, path=["response"])

        assert cast(Any, response.is_closed) is True
