from __future__ import annotations

import re
from pathlib import Path
from typing import Any, cast

from lark import Lark, Token, Transformer, Tree, v_args
from lark.tree import Meta
from typing_extensions import Literal

from pycep import typing as pycep_typing

LARK_GRAMMAR = (Path(__file__).parent / "bicep.lark").read_text()

BICEP_REGISTRY_PATTERN = re.compile(r"br:(?P<registry_name>\w+)\.azurecr\.io/(?P<path>[\w/]+):(?P<tag>[\w.\-]+)")
TEMPLATE_SPEC_PATTERN = re.compile(
    r"ts:(?P<sub_id>[\d\-]+)/(?P<rg_id>[\w._\-()]+)/(?P<name>[\w.\-]+):(?P<version>[\w.\-]+)"
)

VALID_TARGET_SCOPES = {"resourceGroup", "subscription", "managementGroup", "tenant"}


class BicepToJson(Transformer[pycep_typing.BicepJson]):
    def __init__(self, add_line_numbers: bool) -> None:
        self.add_line_numbers = add_line_numbers

        super().__init__()

    ####################
    #
    # start
    #
    ####################

    def start(self, args: list[pycep_typing.ElementResponse]) -> pycep_typing.BicepJson:
        result: pycep_typing.BicepJson = {
            "globals": {
                "scope": {
                    "value": "resourceGroup",
                },
            }
        }

        # defaults are not included in the file
        if self.add_line_numbers:
            result["globals"]["scope"]["__start_line__"] = 0
            result["globals"]["scope"]["__end_line__"] = 0

        for arg in args:
            for key, value in arg.items():
                result.setdefault(key, {})[value["__name__"]] = value["__attrs__"]  # type: ignore[misc, index]

        return result

    ####################
    #
    # elements
    #
    ####################

    @v_args(meta=True)
    def scope(self, meta: Meta, args: tuple[Token]) -> pycep_typing.ScopeResponse:
        value = cast(Literal["resourceGroup", "subscription", "managementGroup", "tenant"], str(args[0])[1:-1])

        if value not in VALID_TARGET_SCOPES:
            raise ValueError(f"target scope is invalid: {value}")

        result: pycep_typing.ScopeResponse = {
            "globals": {
                "__name__": "scope",
                "__attrs__": {
                    "value": value,
                },
            }
        }

        if self.add_line_numbers:
            result["globals"]["__attrs__"]["__start_line__"] = meta.line
            result["globals"]["__attrs__"]["__end_line__"] = meta.end_line

        return result

    @v_args(meta=True)
    def param(
        self, meta: Meta, args: tuple[list[pycep_typing.Decorator] | None, str, str, pycep_typing.PossibleValue | None]
    ) -> pycep_typing.ParamResponse:
        decorators, name, data_type, default = args

        result: pycep_typing.ParamResponse = {
            "parameters": {
                "__name__": name,
                "__attrs__": {
                    "decorators": decorators if decorators else [],
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
    def var(self, meta: Meta, args: tuple[str, pycep_typing.PossibleValue]) -> pycep_typing.VarResponse:
        name, value = args

        result: pycep_typing.VarResponse = {
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
    def output(self, meta: Meta, args: tuple[str, str, pycep_typing.PossibleValue]) -> pycep_typing.OutputResponse:
        name, data_type, value = args

        result: pycep_typing.OutputResponse = {
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
    def resource(
        self,
        meta: Meta,
        args: tuple[list[pycep_typing.Decorator] | None, str, pycep_typing.ApiTypeVersion, dict[str, Any]],
    ) -> pycep_typing.ResourceResponse:
        decorators, name, type_api_pair, config = args

        result: pycep_typing.ResourceResponse = {
            "resources": {
                "__name__": name,
                "__attrs__": {
                    "decorators": decorators if decorators else [],
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
    def module(
        self, meta: Meta, args: tuple[list[pycep_typing.Decorator] | None, str, pycep_typing.ModulePath, dict[str, Any]]
    ) -> pycep_typing.ModuleResponse:
        decorators, name, path, config = args

        result: pycep_typing.ModuleResponse = {
            "modules": {
                "__name__": name,
                "__attrs__": {
                    "decorators": decorators if decorators else [],
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

    def data_type(self, arg: tuple[Token]) -> str:
        return str(arg[0])

    def type_api_pair(self, args: tuple[Token, Token]) -> pycep_typing.ApiTypeVersion:
        type_name, api_version = str(args[0])[1:-1].split("@")
        return {
            "type": str(type_name),
            "api_version": str(api_version),
        }

    def module_path(self, args: tuple[Token]) -> pycep_typing.ModulePath:
        file_path = str(args[0])[1:-1]

        if file_path.startswith("br:"):
            m = re.match(BICEP_REGISTRY_PATTERN, file_path)
            if not m:
                raise ValueError(f"Bicep registry path is invalid: {file_path}")

            br_result: pycep_typing.BicepRegistryModulePath = {
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

            ts_result: pycep_typing.TemplateSpecModulePath = {
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

        local_result: pycep_typing.LocalModulePath = {
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

    def loop(self, args: tuple[pycep_typing.LoopType, str | None, dict[str, Any]]) -> pycep_typing.Loop:
        loop_type, condition, config = args
        return {
            "loop_type": loop_type,
            "condition": condition,
            "config": config,
        }

    def loop_index(self, args: tuple[Token, Token, Token]) -> pycep_typing.LoopIndex:
        idx_name, start_idx, count = args
        return {
            "type": "index",
            "detail": {
                "index_name": str(idx_name),
                "start_index": str(start_idx),
                "count": str(count),
            },
        }

    def loop_array(self, args: tuple[Token, Token]) -> pycep_typing.LoopArray:
        item_name, array_name = args
        return {
            "type": "array",
            "detail": {
                "item_name": str(item_name),
                "array_name": str(array_name),
            },
        }

    def loop_array_index(self, args: tuple[Token, Token, Token]) -> pycep_typing.LoopArrayIndex:
        item_name, idx_name, array_name = args
        return {
            "type": "array_index",
            "detail": {
                "item_name": str(item_name),
                "index_name": str(idx_name),
                "array_name": str(array_name),
            },
        }

    def loop_object(self, args: tuple[Token, Token]) -> pycep_typing.LoopObject:
        item_name, obj_name = args
        return {
            "type": "object",
            "detail": {
                "item_name": str(item_name),
                "object_name": str(obj_name),
            },
        }

    ####################
    #
    # decorators
    #
    ####################

    def decorator(self, args: list[pycep_typing.Decorator]) -> list[pycep_typing.Decorator]:
        return args

    def deco_allowed(self, args: tuple[list[int | str]]) -> pycep_typing.DecoratorAllowed:
        return {
            "type": "allowed",
            "argument": args[0],
        }

    def deco_batch(self, args: tuple[Token]) -> pycep_typing.DecoratorBatchSize:
        return {
            "type": "batchSize",
            "argument": int(args[0]),
        }

    def deco_description(self, args: tuple[Token]) -> pycep_typing.DecoratorDescription:
        return {
            "type": "description",
            "argument": str(args[0]),
        }

    def deco_min_len(self, args: tuple[Token]) -> pycep_typing.DecoratorMinLength:
        return {
            "type": "min_length",
            "argument": int(args[0]),
        }

    def deco_max_len(self, args: tuple[Token]) -> pycep_typing.DecoratorMaxLength:
        return {
            "type": "max_length",
            "argument": int(args[0]),
        }

    def deco_min_val(self, args: tuple[Token]) -> pycep_typing.DecoratorMinValue:
        return {
            "type": "min_value",
            "argument": int(args[0]),
        }

    def deco_max_val(self, args: tuple[Token]) -> pycep_typing.DecoratorMaxValue:
        return {
            "type": "max_value",
            "argument": int(args[0]),
        }

    def deco_metadata(self, args: tuple[dict[str, Any]]) -> pycep_typing.DecoratorMetadata:
        return {
            "type": "metadata",
            "argument": args[0],
        }

    def deco_secure(self, _: Any) -> pycep_typing.DecoratorSecure:
        return {
            "type": "secure",
        }

    ####################
    #
    # operators
    #
    ####################

    def operator(self, args: tuple[pycep_typing.Operators]) -> pycep_typing.Operator:
        return {"operator": args[0]}

    def equals(self, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue]) -> pycep_typing.Equals:
        operand_1, operand_2 = args

        return {
            "type": "equals",
            "operands": {
                "operand_1": operand_1,
                "operand_2": operand_2,
            },
        }

    def not_equals(self, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue]) -> pycep_typing.NotEquals:
        operand_1, operand_2 = args

        return {
            "type": "not_equals",
            "operands": {
                "operand_1": operand_1,
                "operand_2": operand_2,
            },
        }

    def conditional(
        self, args: tuple[Token, pycep_typing.PossibleValue, pycep_typing.PossibleValue]
    ) -> pycep_typing.Conditional:
        condition, true_value, false_value = args

        return {
            "type": "conditional",
            "operands": {
                "condition": str(condition),
                "true_value": true_value,
                "false_value": false_value,
            },
        }

    ####################
    #
    # data types
    #
    ####################

    def array(self, args: list[bool | int | Token]) -> list[bool | int | str]:
        result = [item.value if isinstance(item, Token) else item for item in args]
        return result

    def object(self, args: list[tuple[str, Any]]) -> dict[str, Any]:
        return dict(args)

    def pair(self, args: tuple[str, bool | int | Token]) -> tuple[str, bool | int | str]:
        key, value = args
        return (key, value.value if isinstance(value, Token) else value)

    def key(self, arg: tuple[Token]) -> str:
        return str(arg[0])

    def int(self, arg: tuple[Token]) -> int:
        return int(arg[0])

    def string(self, arg: tuple[Token]) -> str:
        return str(arg[0])

    def multi_line_string(self, arg: tuple[Token]) -> str:
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

    def json(self) -> pycep_typing.BicepJson:
        return BicepToJson(add_line_numbers=self.add_line_numbers).transform(self.tree)

    def print_tree(self) -> str:
        return self.tree.pretty()
