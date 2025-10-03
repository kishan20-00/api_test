# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from api_test import APITest, AsyncAPITest
from tests.utils import assert_matches_type
from api_test._utils import parse_datetime
from api_test.types.api.v1 import (
    File,
    FileListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: APITest) -> None:
        file = client.api.v1.files.create(
            content_type="content_type",
            filename="filename",
            s3_bucket="s3_bucket",
            s3_key="s3_key",
            size=0,
        )
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: APITest) -> None:
        file = client.api.v1.files.create(
            content_type="content_type",
            filename="filename",
            s3_bucket="s3_bucket",
            s3_key="s3_key",
            size=0,
            metadata={"foo": "bar"},
            org_id="org_id",
            owner_id="owner_id",
            status="pending",
            storage_class="storage_class",
            version=0,
        )
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: APITest) -> None:
        response = client.api.v1.files.with_raw_response.create(
            content_type="content_type",
            filename="filename",
            s3_bucket="s3_bucket",
            s3_key="s3_key",
            size=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: APITest) -> None:
        with client.api.v1.files.with_streaming_response.create(
            content_type="content_type",
            filename="filename",
            s3_bucket="s3_bucket",
            s3_key="s3_key",
            size=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: APITest) -> None:
        file = client.api.v1.files.retrieve(
            "key",
        )
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: APITest) -> None:
        response = client.api.v1.files.with_raw_response.retrieve(
            "key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: APITest) -> None:
        with client.api.v1.files.with_streaming_response.retrieve(
            "key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(object, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: APITest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.api.v1.files.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: APITest) -> None:
        file = client.api.v1.files.update(
            file_id="fileId",
        )
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: APITest) -> None:
        file = client.api.v1.files.update(
            file_id="fileId",
            content_type="content_type",
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            filename="filename",
            metadata={"foo": "bar"},
            org_id="org_id",
            owner_id="owner_id",
            s3_bucket="s3_bucket",
            s3_key="s3_key",
            size=0,
            status="pending",
            storage_class="storage_class",
            version=0,
        )
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: APITest) -> None:
        response = client.api.v1.files.with_raw_response.update(
            file_id="fileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: APITest) -> None:
        with client.api.v1.files.with_streaming_response.update(
            file_id="fileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: APITest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.api.v1.files.with_raw_response.update(
                file_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: APITest) -> None:
        file = client.api.v1.files.list()
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: APITest) -> None:
        file = client.api.v1.files.list(
            content_type="content_type",
            created_from=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_to=parse_datetime("2019-12-27T18:11:19.117Z"),
            filename_contains="filename_contains",
            limit=1,
            max_size=0,
            min_size=0,
            org_id="org_id",
            owner_id="owner_id",
            skip=0,
            status="pending",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: APITest) -> None:
        response = client.api.v1.files.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: APITest) -> None:
        with client.api.v1.files.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: APITest) -> None:
        file = client.api.v1.files.delete(
            "fileId",
        )
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: APITest) -> None:
        response = client.api.v1.files.with_raw_response.delete(
            "fileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: APITest) -> None:
        with client.api.v1.files.with_streaming_response.delete(
            "fileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(object, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: APITest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.api.v1.files.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_purge(self, client: APITest) -> None:
        file = client.api.v1.files.delete_purge(
            "fileId",
        )
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_purge(self, client: APITest) -> None:
        response = client.api.v1.files.with_raw_response.delete_purge(
            "fileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_purge(self, client: APITest) -> None:
        with client.api.v1.files.with_streaming_response.delete_purge(
            "fileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(object, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete_purge(self, client: APITest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.api.v1.files.with_raw_response.delete_purge(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_presigned_post(self, client: APITest) -> None:
        file = client.api.v1.files.presigned_post(
            content_type="content_type",
            file_name="file_name",
        )
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_presigned_post(self, client: APITest) -> None:
        response = client.api.v1.files.with_raw_response.presigned_post(
            content_type="content_type",
            file_name="file_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_presigned_post(self, client: APITest) -> None:
        with client.api.v1.files.with_streaming_response.presigned_post(
            content_type="content_type",
            file_name="file_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(object, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_download(self, client: APITest) -> None:
        file = client.api.v1.files.retrieve_download(
            file_id="file_id",
        )
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_download_with_all_params(self, client: APITest) -> None:
        file = client.api.v1.files.retrieve_download(
            file_id="file_id",
            choice="choice",
        )
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_download(self, client: APITest) -> None:
        response = client.api.v1.files.with_raw_response.retrieve_download(
            file_id="file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_download(self, client: APITest) -> None:
        with client.api.v1.files.with_streaming_response.retrieve_download(
            file_id="file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(object, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_download(self, client: APITest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.api.v1.files.with_raw_response.retrieve_download(
                file_id="",
            )


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncAPITest) -> None:
        file = await async_client.api.v1.files.create(
            content_type="content_type",
            filename="filename",
            s3_bucket="s3_bucket",
            s3_key="s3_key",
            size=0,
        )
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAPITest) -> None:
        file = await async_client.api.v1.files.create(
            content_type="content_type",
            filename="filename",
            s3_bucket="s3_bucket",
            s3_key="s3_key",
            size=0,
            metadata={"foo": "bar"},
            org_id="org_id",
            owner_id="owner_id",
            status="pending",
            storage_class="storage_class",
            version=0,
        )
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAPITest) -> None:
        response = await async_client.api.v1.files.with_raw_response.create(
            content_type="content_type",
            filename="filename",
            s3_bucket="s3_bucket",
            s3_key="s3_key",
            size=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAPITest) -> None:
        async with async_client.api.v1.files.with_streaming_response.create(
            content_type="content_type",
            filename="filename",
            s3_bucket="s3_bucket",
            s3_key="s3_key",
            size=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAPITest) -> None:
        file = await async_client.api.v1.files.retrieve(
            "key",
        )
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAPITest) -> None:
        response = await async_client.api.v1.files.with_raw_response.retrieve(
            "key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAPITest) -> None:
        async with async_client.api.v1.files.with_streaming_response.retrieve(
            "key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(object, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAPITest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.api.v1.files.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncAPITest) -> None:
        file = await async_client.api.v1.files.update(
            file_id="fileId",
        )
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncAPITest) -> None:
        file = await async_client.api.v1.files.update(
            file_id="fileId",
            content_type="content_type",
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            filename="filename",
            metadata={"foo": "bar"},
            org_id="org_id",
            owner_id="owner_id",
            s3_bucket="s3_bucket",
            s3_key="s3_key",
            size=0,
            status="pending",
            storage_class="storage_class",
            version=0,
        )
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAPITest) -> None:
        response = await async_client.api.v1.files.with_raw_response.update(
            file_id="fileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAPITest) -> None:
        async with async_client.api.v1.files.with_streaming_response.update(
            file_id="fileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncAPITest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.api.v1.files.with_raw_response.update(
                file_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncAPITest) -> None:
        file = await async_client.api.v1.files.list()
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAPITest) -> None:
        file = await async_client.api.v1.files.list(
            content_type="content_type",
            created_from=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_to=parse_datetime("2019-12-27T18:11:19.117Z"),
            filename_contains="filename_contains",
            limit=1,
            max_size=0,
            min_size=0,
            org_id="org_id",
            owner_id="owner_id",
            skip=0,
            status="pending",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAPITest) -> None:
        response = await async_client.api.v1.files.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAPITest) -> None:
        async with async_client.api.v1.files.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncAPITest) -> None:
        file = await async_client.api.v1.files.delete(
            "fileId",
        )
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAPITest) -> None:
        response = await async_client.api.v1.files.with_raw_response.delete(
            "fileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAPITest) -> None:
        async with async_client.api.v1.files.with_streaming_response.delete(
            "fileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(object, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAPITest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.api.v1.files.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_purge(self, async_client: AsyncAPITest) -> None:
        file = await async_client.api.v1.files.delete_purge(
            "fileId",
        )
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_purge(self, async_client: AsyncAPITest) -> None:
        response = await async_client.api.v1.files.with_raw_response.delete_purge(
            "fileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_purge(self, async_client: AsyncAPITest) -> None:
        async with async_client.api.v1.files.with_streaming_response.delete_purge(
            "fileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(object, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete_purge(self, async_client: AsyncAPITest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.api.v1.files.with_raw_response.delete_purge(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_presigned_post(self, async_client: AsyncAPITest) -> None:
        file = await async_client.api.v1.files.presigned_post(
            content_type="content_type",
            file_name="file_name",
        )
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_presigned_post(self, async_client: AsyncAPITest) -> None:
        response = await async_client.api.v1.files.with_raw_response.presigned_post(
            content_type="content_type",
            file_name="file_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_presigned_post(self, async_client: AsyncAPITest) -> None:
        async with async_client.api.v1.files.with_streaming_response.presigned_post(
            content_type="content_type",
            file_name="file_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(object, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_download(self, async_client: AsyncAPITest) -> None:
        file = await async_client.api.v1.files.retrieve_download(
            file_id="file_id",
        )
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_download_with_all_params(self, async_client: AsyncAPITest) -> None:
        file = await async_client.api.v1.files.retrieve_download(
            file_id="file_id",
            choice="choice",
        )
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_download(self, async_client: AsyncAPITest) -> None:
        response = await async_client.api.v1.files.with_raw_response.retrieve_download(
            file_id="file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_download(self, async_client: AsyncAPITest) -> None:
        async with async_client.api.v1.files.with_streaming_response.retrieve_download(
            file_id="file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(object, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_download(self, async_client: AsyncAPITest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.api.v1.files.with_raw_response.retrieve_download(
                file_id="",
            )
