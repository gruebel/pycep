from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Dict, List, Tuple, Union

from lark import Lark, Token, Transformer, Tree, v_args
from lark.tree import Meta
from typing_extensions import Literal

from pycep.typing import (
    ApiTypeVersion,
    BicepRegistryModulePath,
    LocalModulePath,
    ModulePath,
    ModuleResponse,
    OutputResponse,
    ParamResponse,
    PossibleValue,
    ResourceResponse,
    TemplateSpecModulePath,
    VarResponse,
)

LARK_GRAMMAR = (Path(__file__).parent / "bicep.lark").read_text()

BICEP_REGISTRY_PATTERN = re.compile(r"br:(?P<registry_name>\w+)\.azurecr\.io/(?P<path>[\w/]+):(?P<tag>[\w.\-]+)")
TEMPLATE_SPEC_PATTERN = re.compile(
    r"ts:(?P<sub_id>[\d\-]+)/(?P<rg_id>[\w._\-()]+)/(?P<name>[\w.\-]+):(?P<version>[\w.\-]+)"
)


class BicepToJson(Transformer[Dict[str, Any]]):
    def __init__(self, add_line_numbers: bool) -> None:
        self.add_line_numbers = add_line_numbers

        super().__init__()

    ####################
    #
    # start
    #
    ####################

    def start(self, args: List[Dict[str, Any]]) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        for arg in args:
            for key, value in arg.items():
                result.setdefault(key, {})[value["__name__"]] = value["__attrs__"]

        return result

    ####################
    #
    # elements
    #
    ####################

    @v_args(meta=True)
    def param(self, meta: Meta, args: tuple[str, str, PossibleValue | None]) -> ParamResponse:
        name, data_type, default = args

        result: ParamResponse = {
            "parameters": {
                "__name__": name,
                "__attrs__": {
                    "type": data_type,
                    "default": default,
                },
            }
        }

        if self.add_line_numbers:
            result["parameters"]["__attrs__"]["__start_line__"] = meta.line
            result["parameters"]["__attrs__"]["__end_line__"] = meta.end_line

        return result

    @v_args(meta=True)
    def var(self, meta: Meta, args: tuple[str, PossibleValue]) -> VarResponse:
        name, value = args

        result: VarResponse = {
            "variables": {
                "__name__": name,
                "__attrs__": {
                    "value": value,
                },
            }
        }

        if self.add_line_numbers:
            result["variables"]["__attrs__"]["__start_line__"] = meta.line
            result["variables"]["__attrs__"]["__end_line__"] = meta.end_line

        return result

    @v_args(meta=True)
    def output(self, meta: Meta, args: tuple[str, str, PossibleValue]) -> OutputResponse:
        name, data_type, value = args

        result: OutputResponse = {
            "outputs": {
                "__name__": name,
                "__attrs__": {
                    "type": data_type,
                    "value": value,
                },
            }
        }

        if self.add_line_numbers:
            result["outputs"]["__attrs__"]["__start_line__"] = meta.line
            result["outputs"]["__attrs__"]["__end_line__"] = meta.end_line

        return result

    @v_args(meta=True)
    def resource(self, meta: Meta, args: tuple[str, ApiTypeVersion, Dict[str, Any]]) -> ResourceResponse:
        name, type_api_pair, config = args

        result: ResourceResponse = {
            "resources": {
                "__name__": name,
                "__attrs__": {
                    **type_api_pair,  # type: ignore[misc] # https://github.com/python/mypy/issues/11753
                    "config": config,
                },
            }
        }

        if self.add_line_numbers:
            result["resources"]["__attrs__"]["__start_line__"] = meta.line
            result["resources"]["__attrs__"]["__end_line__"] = meta.end_line

        return result

    @v_args(meta=True)
    def module(self, meta: Meta, args: Tuple[str, ModulePath, Dict[str, Any]]) -> ModuleResponse:
        name, path, config = args

        result: ModuleResponse = {
            "modules": {
                "__name__": name,
                "__attrs__": {
                    **path,  # type: ignore[misc] # https://github.com/python/mypy/issues/11753
                    "config": config,
                },
            }
        }

        if self.add_line_numbers:
            result["modules"]["__attrs__"]["__start_line__"] = meta.line
            result["modules"]["__attrs__"]["__end_line__"] = meta.end_line

        return result

    ####################
    #
    # element type extras
    #
    ####################

    def data_type(self, arg: Tuple[Token]) -> str:
        return str(arg[0])

    def type_api_pair(self, args: Tuple[Token, Token]) -> Dict[str, str]:
        type_name, api_version = args
        return {"type": str(type_name), "api_version": str(api_version)}

    def module_path(self, args: Tuple[Token]) -> ModulePath:
        file_path = str(args[0])[1:-1]

        if file_path.startswith("br:"):
            m = re.match(BICEP_REGISTRY_PATTERN, file_path)
            if not m:
                raise ValueError(f"Bicep registry path is invalid: {file_path}")

            br_result: BicepRegistryModulePath = {
                "type": "bicep_registry",
                "detail": {
                    "full": file_path[3:],
                    "registry_name": m.group("registry_name"),
                    "path": m.group("path"),
                    "tag": m.group("tag"),
                },
            }
            return br_result
        elif file_path.startswith("ts:"):
            m = re.match(TEMPLATE_SPEC_PATTERN, file_path)
            if not m:
                raise ValueError(f"Template spec path is invalid: {file_path}")

            ts_result: TemplateSpecModulePath = {
                "type": "template_spec",
                "detail": {
                    "full": file_path[3:],
                    "subscription_id": m.group("sub_id"),
                    "resource_group_id": m.group("rg_id"),
                    "name": m.group("name"),
                    "version": m.group("version"),
                },
            }
            return ts_result

        local_result: LocalModulePath = {
            "type": "local",
            "detail": {
                "full": file_path,
                "path": file_path,
            },
        }
        return local_result

    ####################
    #
    # loops
    #
    ####################

    def loop(self, args: Tuple[Token, Token, Token]) -> Dict[str, Any]:
        loop_type, condition, config = args
        return {
            "loop_type": loop_type,
            "condition": condition,
            "config": config,
        }

    def loop_range(self, args: Tuple[Token, Token, Token]) -> Dict[str, Any]:
        idx_name, start_idx, count = args
        return {
            "type": "index",
            "detail": {
                "index_name": str(idx_name),
                "start_index": str(start_idx),
                "count": str(count),
            },
        }

    def loop_array(self, args: Tuple[Token, Token]) -> Dict[str, Any]:
        item_name, array_name = args
        return {
            "type": "array",
            "detail": {
                "item_name": str(item_name),
                "array_name": str(array_name),
            },
        }

    def loop_array_index(self, args: Tuple[Token, Token, Token]) -> Dict[str, Any]:
        item_name, idx_name, array_name = args
        return {
            "type": "array",
            "detail": {
                "item_name": str(item_name),
                "index_name": str(idx_name),
                "array_name": str(array_name),
            },
        }

    ####################
    #
    # data types
    #
    ####################

    def array(self, args: List[Union[bool, int, Token]]) -> List[Union[bool, int, str]]:
        result = [item.value if isinstance(item, Token) else item for item in args]
        return result

    def object(self, args: List[Tuple[str, Any]]) -> Dict[str, Any]:
        return dict(args)

    def pair(self, args: Tuple[str, Union[bool, int, Token]]) -> Tuple[str, Union[bool, int, str]]:
        key, value = args
        return (key, value.value if isinstance(value, Token) else value)

    def key(self, arg: Tuple[Token]) -> str:
        return str(arg[0])

    def int(self, arg: Tuple[Token]) -> int:
        return int(arg[0])

    def string(self, arg: Tuple[Token]) -> str:
        return str(arg[0])

    def multi_line_string(self, arg: Tuple[Token]) -> str:
        value = arg[0].value[3:-3]
        value = value[1:] if value.startswith("\n") else value
        return f"'{value}'"

    def true(self, _: Any) -> Literal[True]:
        return True

    def false(self, _: Any) -> Literal[False]:
        return False


class BicepParser:
    def __init__(self, file_path: Path, add_line_numbers: bool = False) -> None:
        self.file_path = file_path
        self.add_line_numbers = add_line_numbers

        self.tree = self._create_tree()

    def _create_tree(self) -> Tree:
        content = self.file_path.read_text()
        lark_parser = Lark(grammar=LARK_GRAMMAR, parser="lalr", propagate_positions=True)

        return lark_parser.parse(content)

    def json(self) -> Dict[str, Any]:
        return BicepToJson(add_line_numbers=self.add_line_numbers).transform(self.tree)

    def print_tree(self) -> str:
        return self.tree.pretty()
