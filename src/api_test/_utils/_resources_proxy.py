from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `api_test.resources` module.

    This is used so that we can lazily import `api_test.resources` only when
    needed *and* so that users can just import `api_test` and reference `api_test.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("api_test.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
