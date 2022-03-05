from __future__ import annotations

from importlib import resources
from pathlib import Path

from lark import Lark, Token, Tree

from pycep import typing as pycep_typing

from .transformer import BicepToJson

LARK_GRAMMAR = resources.read_text(__package__, "bicep.lark")


class BicepParser:
    """Wrapper class for Lark"""

    def __init__(self, *, add_line_numbers: bool = False, cache: bool = True) -> None:
        self.add_line_numbers = add_line_numbers
        self.lark_parser = Lark(grammar=LARK_GRAMMAR, parser="lalr", propagate_positions=True, regex=True, cache=cache)

    def parse(self, *, text: str | None = None, file_path: Path | None = None) -> pycep_typing.BicepJson:
        tree = self._create_tree(text=text, file_path=file_path)
        return BicepToJson(add_line_numbers=self.add_line_numbers).transform(tree)

    def create_tree(self, *, text: str | None = None, file_path: Path | None = None) -> str:
        tree = self._create_tree(text=text, file_path=file_path)
        return tree.pretty()

    def _create_tree(self, text: str | None, file_path: Path | None) -> Tree[Token]:
        if text and file_path:
            raise TypeError("Either 'text' or 'file_path' can be set")

        if text:
            bicep_text = text
        elif file_path:
            bicep_text = file_path.read_text()
        else:
            raise TypeError("Either 'text' or 'file_path' has to be set")

        return self.lark_parser.parse(bicep_text)
