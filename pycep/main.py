from __future__ import annotations

from importlib import resources
from pathlib import Path

from lark import Lark, Tree

from pycep import typing as pycep_typing

from .transformer import BicepToJson

LARK_GRAMMAR = resources.read_text(__package__, "bicep.lark")


class BicepParser:
    lark_parser = Lark(grammar=LARK_GRAMMAR, parser="lalr", propagate_positions=True, regex=True)

    def __init__(self, file_path: Path, add_line_numbers: bool = False) -> None:
        self.file_path = file_path
        self.add_line_numbers = add_line_numbers

        self.tree = self._create_tree()

    def _create_tree(self) -> Tree:
        content = self.file_path.read_text()

        return BicepParser.lark_parser.parse(content)

    def json(self) -> pycep_typing.BicepJson:
        return BicepToJson(add_line_numbers=self.add_line_numbers).transform(self.tree)

    def print_tree(self) -> str:
        return self.tree.pretty()
