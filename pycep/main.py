from __future__ import annotations

from importlib import resources
from pathlib import Path

from lark import Lark, Tree

from pycep import typing as pycep_typing

from .transformer import BicepToJson

LARK_GRAMMAR = resources.read_text(__package__, "bicep.lark")


class BicepParser:
    lark_parser = Lark(grammar=LARK_GRAMMAR, parser="lalr", propagate_positions=True, regex=True)

    def __init__(
        self, *, text: str | None = None, file_path: Path | None = None, add_line_numbers: bool = False
    ) -> None:
        if text and file_path:
            raise TypeError("Either 'text' or 'file_path' can be set")

        if text:
            bicep_text = text
        elif file_path:
            bicep_text = file_path.read_text()
        else:
            raise TypeError("Either 'text' or 'file_path' has to be set")

        self.add_line_numbers = add_line_numbers
        self.tree = self._create_tree(bicep_text)

    def _create_tree(self, text: str) -> Tree:
        return BicepParser.lark_parser.parse(text)

    def json(self) -> pycep_typing.BicepJson:
        return BicepToJson(add_line_numbers=self.add_line_numbers).transform(self.tree)

    def print_tree(self) -> str:
        return self.tree.pretty()
