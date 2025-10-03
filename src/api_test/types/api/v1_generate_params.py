# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V1GenerateParams", "Message"]


class V1GenerateParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]

    max_tokens: int

    model: str

    seed: Optional[int]

    stop_sequence: Annotated[Optional[str], PropertyInfo(alias="stopSequence")]

    stream: bool

    temperature: float

    top_k: int

    top_p: float


class Message(TypedDict, total=False):
    role: Required[str]

    content: Union[str, Iterable[Dict[str, object]], None]

    function_call: Optional[Dict[str, object]]

    name: Optional[str]

    refusal: Optional[str]

    tool_call_id: Optional[str]

    tool_calls: Optional[Iterable[Dict[str, object]]]
