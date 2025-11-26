from __future__ import annotations

from typing import TYPE_CHECKING

from pycep.models import BicepElement

if TYPE_CHECKING:
    from lark import Token


def transform_string_token(value: Token) -> str | BicepElement:
    """Transforms string typed Token to a `str` or `BicepElement`.

    Additionally, removes surrounding single quotes.
    """
    if value.type == "MULTI_LINE_STRING":
        return sanitize_multi_line_string_token(value)

    if value.type not in ("QUOTED_STRING", "QUOTED_INTERPOLATION"):
        return BicepElement(value)

    return str(value)[1:-1]


def sanitize_multi_line_string_token(value: Token) -> str:
    """Sanitizes multi-line string typed Token."""
    return str(value)[3:-3].removeprefix("\n")
