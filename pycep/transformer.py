from __future__ import annotations

import itertools
import re
from typing import TYPE_CHECKING, Any, Literal, cast

from lark import Token, Transformer, v_args

from pycep import typing as pycep_typing
from pycep.models import BicepElement
from pycep.rules.decorators import DECORATORS, UNKNOWN_DECORATOR
from pycep.rules.functions import FUNCTIONS, UNKNOWN_FUNCTION
from pycep.utils import sanitize_multi_line_string_token, transform_string_token

if TYPE_CHECKING:
    from lark.tree import Meta


BICEP_REGISTRY_ALIAS_PATTERN = re.compile(r"br/(?P<alias>[\w]+):(?P<path>[\w/\-.]+):(?P<tag>[\w.\-]+)")
PUBLIC_BICEP_REGISTRY_PATTERN = re.compile(r"br:mcr\.microsoft\.com/(?P<path>[\w/\-]+):(?P<tag>[\w.\-]+)")
PRIVATE_BICEP_REGISTRY_PATTERN = re.compile(
    r"br:(?P<registry_name>\w+)\.azurecr\.io/(?P<path>[\w/\-.]+):(?P<tag>[\w.\-]+)"
)
TEMPLATE_SPEC_ALIAS_PATTERN = re.compile(r"ts/(?P<alias>[\w]+):(?P<path>[\w/\-]+):(?P<tag>[\w.\-]+)")
TEMPLATE_SPEC_PATTERN = re.compile(
    r"ts:(?P<sub_id>[\d\-]+)/(?P<rg_id>[\w._\-()]+)/(?P<name>[\w.\-]+):(?P<version>[\w.\-]+)"
)

VALID_TARGET_SCOPES = {"resourceGroup", "subscription", "managementGroup", "tenant"}


class BicepToJson(Transformer[Token, pycep_typing.BicepJson]):
    def __init__(self, add_line_numbers: bool) -> None:
        self.add_line_numbers = add_line_numbers

        self.imports: list[pycep_typing.ImportResponse] = []
        self.child_resources: list[pycep_typing.ResourceResponse] = []

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

        for arg in itertools.chain(args, self.imports, self.child_resources):
            if not arg:
                # very unlikely this will happen in a real Bicep file, but in test files possible
                continue
            for key, value in arg.items():
                result.setdefault(key, {})[value["__name__"]] = value["__attrs__"]  # ty: ignore[not-subscriptable, no-matching-overload]

        return result

    ####################
    #
    # elements
    #
    ####################

    @v_args(meta=True)
    def scope(self, meta: Meta, args: tuple[Token]) -> pycep_typing.ScopeResponse:
        value = cast('Literal["resourceGroup", "subscription", "managementGroup", "tenant"]', str(args[0])[1:-1])

        if value not in VALID_TARGET_SCOPES:  # pragma: no cover
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
    def custom_import(
        self, meta: Meta, args: tuple[pycep_typing.ImportNameAlias, pycep_typing.ImportNameAlias, Token]
    ) -> None:
        # the import statement parsing is slightly overload to support namespace imports,
        # which don't have a file reference
        if len(args) == 1:
            result: pycep_typing._Import = {
                "__name__": transform_string_token(args[0]),
                "__attrs__": {},
            }
            self.imports.append(
                {
                    "imports": result,
                }
            )
            return

        # to make typing easy, there are two import types defined, but it could be more
        *name_alias_pairs, file_path = args

        for name_alias in name_alias_pairs:
            result: pycep_typing._Import = {
                "__name__": str(name_alias["name"]),
                "__attrs__": {
                    "file_path": transform_string_token(file_path),
                },
            }

            if alias := name_alias.get("alias"):
                result["__attrs__"]["alias"] = str(alias)

            if self.add_line_numbers:
                result["__attrs__"]["__start_line__"] = meta.line
                result["__attrs__"]["__end_line__"] = meta.end_line

            self.imports.append(
                {
                    "imports": result,
                }
            )

    @v_args(meta=True)
    def extension(
        self, meta: Meta, args: tuple[str, dict[str, Any] | None, str | None]
    ) -> pycep_typing.ExtensionResponse:
        name, config, alias = args

        result: pycep_typing.ExtensionResponse = {
            "extensions": {
                "__name__": str(name),
                "__attrs__": {},
            }
        }

        if config:
            result["extensions"]["__attrs__"]["config"] = config

        if alias:
            result["extensions"]["__attrs__"]["alias"] = str(alias)

        if self.add_line_numbers:
            result["extensions"]["__attrs__"]["__start_line__"] = meta.line
            result["extensions"]["__attrs__"]["__end_line__"] = meta.end_line

        return result

    @v_args(meta=True)
    def metadata(self, meta: Meta, args: tuple[str, str]) -> pycep_typing.MetadataResponse:
        name, value = args

        result: pycep_typing.MetadataResponse = {
            "metadata": {
                "__name__": str(name),
                "__attrs__": {
                    "value": value,
                },
            }
        }

        if self.add_line_numbers:
            result["metadata"]["__attrs__"]["__start_line__"] = meta.line
            result["metadata"]["__attrs__"]["__end_line__"] = meta.end_line

        return result

    @v_args(meta=True)
    def param(
        self, meta: Meta, args: tuple[list[pycep_typing.Decorator] | None, str, str, pycep_typing.PossibleNoneValue]
    ) -> pycep_typing.ParamResponse:
        decorators, name, data_type, default = args

        result: pycep_typing.ParamResponse = {
            "parameters": {
                "__name__": str(name),
                "__attrs__": {
                    "decorators": decorators or [],
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
    def var(
        self,
        meta: Meta,
        args: tuple[list[pycep_typing.Decorator] | None, Token, str | None, pycep_typing.PossibleValue],
    ) -> pycep_typing.VarResponse:
        decorators, name, data_type, value = args

        result: pycep_typing.VarResponse = {
            "variables": {
                "__name__": str(name),
                "__attrs__": {
                    "decorators": decorators or [],
                    "value": value,
                },
            }
        }

        if data_type:
            result["variables"]["__attrs__"]["type"] = data_type

        if self.add_line_numbers:
            result["variables"]["__attrs__"]["__start_line__"] = meta.line
            result["variables"]["__attrs__"]["__end_line__"] = meta.end_line

        return result

    @v_args(meta=True)
    def output(
        self, meta: Meta, args: tuple[list[pycep_typing.Decorator] | None, str, str, pycep_typing.PossibleValue]
    ) -> pycep_typing.OutputResponse:
        decorators, name, data_type, value = args

        result: pycep_typing.OutputResponse = {
            "outputs": {
                "__name__": str(name),
                "__attrs__": {
                    "decorators": decorators or [],
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
        args: tuple[
            list[pycep_typing.Decorator] | None, Token, pycep_typing.ApiTypeVersion, Token | None, dict[str, Any]
        ],
    ) -> pycep_typing.ResourceResponse:
        decorators, name, type_api_pair, existing, config = args
        name_str = str(name)

        self.process_child_resource(parent_resource_name=name_str, parent_type_api_pair=type_api_pair, config=config)

        result: pycep_typing.ResourceResponse = {
            "resources": {
                "__name__": name_str,
                "__attrs__": {
                    "decorators": decorators or [],
                    "type": type_api_pair["type"],
                    "api_version": type_api_pair["api_version"],
                    "existing": bool(existing),
                    "config": config,
                },
            }
        }

        if self.add_line_numbers:
            result["resources"]["__attrs__"]["__start_line__"] = meta.line
            result["resources"]["__attrs__"]["__end_line__"] = meta.end_line

        return result

    @v_args(meta=True)
    def child_resource(
        self, meta: Meta, args: tuple[Token, Token, Token | None, dict[str, Any]]
    ) -> tuple[Literal["__child_resource__"], pycep_typing.Resource]:
        name, type_name, existing, config = args

        result: pycep_typing.Resource = {
            "__name__": str(name),
            "__attrs__": {
                "decorators": [],
                "type": str(type_name)[1:-1],
                "api_version": "",  # will be set later with the parent resource api version
                "existing": bool(existing),
                "config": config,
            },
        }

        if self.add_line_numbers:
            result["__attrs__"]["__start_line__"] = meta.line
            # remove one line, because the new line is counted for child resources
            result["__attrs__"]["__end_line__"] = meta.end_line - 1

        return "__child_resource__", result

    @v_args(meta=True)
    def module(
        self, meta: Meta, args: tuple[list[pycep_typing.Decorator] | None, str, pycep_typing.ModulePath, dict[str, Any]]
    ) -> pycep_typing.ModuleResponse:
        decorators, name, path, config = args

        result: pycep_typing.ModuleResponse = {
            "modules": {
                "__name__": str(name),
                "__attrs__": {
                    "decorators": decorators or [],
                    "type": path["type"],
                    "detail": path["detail"],
                    "config": config,
                },
            }
        }

        if self.add_line_numbers:
            result["modules"]["__attrs__"]["__start_line__"] = meta.line
            result["modules"]["__attrs__"]["__end_line__"] = meta.end_line

        return result

    @v_args(meta=True)
    def custom_type(
        self, meta: Meta, args: tuple[list[pycep_typing.Decorator] | None, Token, pycep_typing.PossibleValue]
    ) -> pycep_typing.TypeResponse:
        decorators, name, value = args

        result: pycep_typing.TypeResponse = {
            "types": {
                "__name__": str(name),
                "__attrs__": {
                    "decorators": decorators or [],
                    "value": value,
                },
            }
        }

        if self.add_line_numbers:
            result["types"]["__attrs__"]["__start_line__"] = meta.line
            result["types"]["__attrs__"]["__end_line__"] = meta.end_line

        return result

    @v_args(meta=True)
    def custom_func(
        self,
        meta: Meta,
        args: tuple[
            list[pycep_typing.Decorator] | None,
            Token,
            pycep_typing.PossibleValue,
            pycep_typing.PossibleValue,
        ],
    ) -> pycep_typing.FunctionResponse:
        decorators, name, *arg_type_pairs, return_type, expression = args

        result: pycep_typing.FunctionResponse = {
            "functions": {
                "__name__": str(name),
                "__attrs__": {
                    "decorators": decorators or [],
                    # TODO: change `zip` to `itertools.batched` when updating to Python 3.12
                    "args": {
                        str(arg_name): arg_type for arg_name, arg_type in zip(*[iter(arg_type_pairs)] * 2, strict=True)
                    },
                    "type": return_type,
                    "expression": expression,
                },
            }
        }

        if self.add_line_numbers:
            result["functions"]["__attrs__"]["__start_line__"] = meta.line
            result["functions"]["__attrs__"]["__end_line__"] = meta.end_line

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
            # check if it's referencing the official public registry
            m = re.match(PUBLIC_BICEP_REGISTRY_PATTERN, file_path)
            if m:
                is_public = True
                registry_name = "mcr.microsoft.com"
            else:
                # check if it's referencing a privvte registry
                m = re.match(PRIVATE_BICEP_REGISTRY_PATTERN, file_path)
                if m:
                    is_public = False
                    registry_name = m.group("registry_name")
                else:  # pragma: no cover
                    raise ValueError(f"Bicep registry path is invalid: {file_path}")

            br_result: pycep_typing.BicepRegistryModulePath = {
                "type": "bicep_registry",
                "detail": {
                    "full": file_path[3:],
                    "registry_name": registry_name,
                    "path": m.group("path"),
                    "tag": m.group("tag"),
                    "public": is_public,
                },
            }
            return br_result
        elif file_path.startswith("br/"):
            m = re.match(BICEP_REGISTRY_ALIAS_PATTERN, file_path)
            if not m:  # pragma: no cover
                raise ValueError(f"Bicep registry alias is invalid: {file_path}")

            alias = m.group("alias")
            is_public = False

            # check if it's the alias of the official public registry
            if alias == "public":
                is_public = True

            br_alias_result: pycep_typing.BicepRegistryAliasModulePath = {
                "type": "bicep_registry_alias",
                "detail": {
                    "full": file_path[3:],
                    "alias": alias,
                    "path": m.group("path"),
                    "tag": m.group("tag"),
                    "public": is_public,
                },
            }
            return br_alias_result
        elif file_path.startswith("ts:"):
            m = re.match(TEMPLATE_SPEC_PATTERN, file_path)
            if not m:  # pragma: no cover
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
        elif file_path.startswith("ts/"):
            m = re.match(TEMPLATE_SPEC_ALIAS_PATTERN, file_path)
            if not m:  # pragma: no cover
                raise ValueError(f"Template spec alias is invalid: {file_path}")

            ts_alias_result: pycep_typing.TemplateSpecAliasModulePath = {
                "type": "template_spec_alias",
                "detail": {
                    "full": file_path[3:],
                    "alias": m.group("alias"),
                    "path": m.group("path"),
                    "tag": m.group("tag"),
                },
            }
            return ts_alias_result

        local_result: pycep_typing.LocalModulePath = {
            "type": "local",
            "detail": {
                "full": file_path,
                "path": file_path,
            },
        }
        return local_result

    def import_alias(self, args: tuple[Token, ...]) -> pycep_typing.ImportNameAlias:
        name, alias = args

        result: pycep_typing.ImportNameAlias = {"name": str(name)}

        if alias:
            result["alias"] = str(alias)

        return result

    def type_value(self, args: tuple[pycep_typing.PossibleNoneValue, ...]) -> str:
        # this is only triggered, when a union type was found, ex. "'bicep' | 'arm' | 'azure'"
        return " | ".join(str(arg) for arg in args)

    ####################
    #
    # loops
    #
    ####################

    def loop(self, args: tuple[pycep_typing.LoopType, str | None, dict[str, Any]]) -> pycep_typing.Loop:
        loop_type, condition, config = args

        if isinstance(condition, dict) and (func := condition.get("function", {})).get("type") == "if":
            condition = func["parameters"]["arg_1"]

        return {
            "loop_type": loop_type,
            "condition": condition,
            "config": config,
        }

    def loop_array(self, args: tuple[Token, pycep_typing.PossibleValue]) -> pycep_typing.LoopArray:
        item_name, array_name = args
        return {
            "type": "array",
            "detail": {
                "item_name": str(item_name),
                "array_name": array_name,
            },
        }

    def loop_array_index(self, args: tuple[Token, Token, Token]) -> pycep_typing.LoopArrayIndex:
        item_name, idx_name, array_name = args
        return {
            "type": "array_index",
            "detail": {
                "item_name": str(item_name),
                "index_name": str(idx_name),
                "array_name": array_name,
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
    # deploy condition
    #
    ####################

    def deploy_condition(self, args: tuple[pycep_typing.PossibleValue, dict[str, Any]]) -> pycep_typing.DeployCondition:
        condition, config = args
        return {
            "condition": condition,
            "config": config,
        }

    ####################
    #
    # decorators
    #
    ####################

    def decorator(self, args: list[pycep_typing.Decorator]) -> pycep_typing.Decorator:
        deco_name, *params = args
        deco_name = str(deco_name)

        deco_def = DECORATORS.get(deco_name, UNKNOWN_DECORATOR)
        return deco_def(deco_name, params)

    def decorators(self, args: list[pycep_typing.Decorator]) -> list[pycep_typing.Decorator]:
        return args

    ####################
    #
    # functions
    #
    ####################

    def function(self, args: tuple[pycep_typing.PossibleValue, ...]) -> pycep_typing.Function:
        func_name, *params = args
        func_name = str(func_name).removesuffix("(")

        func_def = FUNCTIONS.get(func_name, UNKNOWN_FUNCTION)
        func_data = func_def(func_name, params)

        return {"function": func_data}

    ####################
    #
    # operators - comparison
    #
    ####################

    def operator(self, args: tuple[pycep_typing.Operators]) -> pycep_typing.Operator:
        return {"operator": args[0]}

    def greater_than_or_equals(self, args: tuple[int | str, int | str]) -> pycep_typing.GreaterThanOrEquals:
        operand_1, operand_2 = args

        return {
            "type": "greater_than_or_equals",
            "operands": {
                "operand_1": operand_1,
                "operand_2": operand_2,
            },
        }

    def greater_than(self, args: tuple[int | str, int | str]) -> pycep_typing.GreaterThan:
        operand_1, operand_2 = args

        return {
            "type": "greater_than",
            "operands": {
                "operand_1": operand_1,
                "operand_2": operand_2,
            },
        }

    def less_than_or_equals(self, args: tuple[int | str, int | str]) -> pycep_typing.LessThanOrEquals:
        operand_1, operand_2 = args

        return {
            "type": "less_than_or_equals",
            "operands": {
                "operand_1": operand_1,
                "operand_2": operand_2,
            },
        }

    def less_than(self, args: tuple[int | str, int | str]) -> pycep_typing.LessThan:
        operand_1, operand_2 = args

        return {
            "type": "less_than",
            "operands": {
                "operand_1": operand_1,
                "operand_2": operand_2,
            },
        }

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

    def equals_case_insens(self, args: tuple[str, str]) -> pycep_typing.EqualsCaseInsensitive:
        operand_1, operand_2 = args

        return {
            "type": "equals_case_insensitive",
            "operands": {
                "operand_1": operand_1,
                "operand_2": operand_2,
            },
        }

    def not_equals_case_insens(self, args: tuple[str, str]) -> pycep_typing.NotEqualsCaseInsensitive:
        operand_1, operand_2 = args

        return {
            "type": "not_equals_case_insensitive",
            "operands": {
                "operand_1": operand_1,
                "operand_2": operand_2,
            },
        }

    ####################
    #
    # Operators - logical
    #
    ####################

    def and_op(self, args: tuple[bool | str, ...]) -> pycep_typing.And:
        operand_1, operand_2, *operand_x = args

        return {
            "type": "and",
            "operands": {
                "operand_1": operand_1,
                "operand_2": operand_2,
                **{f"operand_{idx + 3}": op for idx, op in enumerate(operand_x)},
            },
        }

    def or_op(self, args: tuple[bool | str, ...]) -> pycep_typing.Or:
        operand_1, operand_2, *operand_x = args

        return {
            "type": "or",
            "operands": {
                "operand_1": operand_1,
                "operand_2": operand_2,
                **{f"operand_{idx + 3}": op for idx, op in enumerate(operand_x)},
            },
        }

    def not_op(self, args: tuple[bool | str]) -> pycep_typing.Not:
        return {
            "type": "not",
            "operands": {
                "bool_value": args[0],
            },
        }

    def coalesce(self, args: tuple[pycep_typing.PossibleValue, ...]) -> pycep_typing.Coalesce:
        operand_1, operand_2, *operand_x = args

        return {
            "type": "coalesce",
            "operands": {
                "operand_1": operand_1,
                "operand_2": operand_2,
                **{f"operand_{idx + 3}": op for idx, op in enumerate(operand_x)},
            },
        }

    def conditional(
        self, args: tuple[Token | pycep_typing.PossibleValue, pycep_typing.PossibleValue, pycep_typing.PossibleValue]
    ) -> pycep_typing.Conditional:
        condition, true_value, false_value = args

        return {
            "type": "conditional",
            "operands": {
                "condition": condition,
                "true_value": true_value,
                "false_value": false_value,
            },
        }

    ####################
    #
    # operators - numeric
    #
    ####################

    def add(self, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue]) -> pycep_typing.Add:
        operand_1, operand_2 = args

        return {
            "type": "add",
            "operands": {
                "operand_1": operand_1,
                "operand_2": operand_2,
            },
        }

    def divide(self, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue]) -> pycep_typing.Divide:
        operand_1, operand_2 = args

        return {
            "type": "divide",
            "operands": {
                "operand_1": operand_1,
                "operand_2": operand_2,
            },
        }

    def minus(self, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.Minus:
        return {
            "type": "minus",
            "operands": {
                "integer_value": args[0],
            },
        }

    def modulo(self, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue]) -> pycep_typing.Modulo:
        operand_1, operand_2 = args

        return {
            "type": "modulo",
            "operands": {
                "operand_1": operand_1,
                "operand_2": operand_2,
            },
        }

    def multiply(self, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue]) -> pycep_typing.Multiply:
        operand_1, operand_2 = args

        return {
            "type": "multiply",
            "operands": {
                "operand_1": operand_1,
                "operand_2": operand_2,
            },
        }

    def substract(self, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue]) -> pycep_typing.Substract:
        operand_1, operand_2 = args

        return {
            "type": "substract",
            "operands": {
                "operand_1": operand_1,
                "operand_2": operand_2,
            },
        }

    ####################
    #
    # operators - accessor
    #
    ####################

    def index_accessor(
        self, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue]
    ) -> pycep_typing.IndexAccessor:
        arg_1, arg_2 = args
        return {"type": "index_accessor", "operands": {"operand_1": arg_1, "operand_2": arg_2}}

    def function_accessor(self, args: tuple[pycep_typing.PossibleValue, ...]) -> pycep_typing.FunctionAccessor:
        arg_1, func_name, *arg_x = args
        return {
            "type": "function_accessor",
            "operands": {
                "operand_1": arg_1,
                "func_name": str(func_name),
                **{f"operand_{idx + 2}": extra for idx, extra in enumerate(arg_x) if extra},
            },
        }

    def nested_resource_accessor(
        self, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue]
    ) -> pycep_typing.NestedResourceAccessor:
        arg_1, arg_2 = args
        return {"type": "nested_resource_accessor", "operands": {"operand_1": arg_1, "operand_2": arg_2}}

    def property_accessor(
        self, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue]
    ) -> pycep_typing.PropertyAccessor:
        arg_1, arg_2 = args
        return {"type": "property_accessor", "operands": {"operand_1": arg_1, "operand_2": arg_2}}

    ####################
    #
    # data types
    #
    ####################

    def array(self, args: list[bool | int | Token]) -> list[bool | int | str]:
        return [item.value if isinstance(item, Token) else item for item in args]

    def object(self, args: list[tuple[str, Any]]) -> dict[str, Any]:
        return dict(args)

    def pair(self, args: tuple[str, bool | int | Token]) -> tuple[str, bool | int | str]:
        key, value = args
        return key, value.value if isinstance(value, Token) else value

    def key(self, arg: tuple[Token]) -> str:
        return str(arg[0])

    def int_type(self, arg: tuple[Token]) -> int:
        return int(arg[0])

    def string(self, arg: tuple[Token]) -> str:
        return transform_string_token(arg[0])

    def multi_line_string(self, arg: tuple[Token]) -> str:
        return sanitize_multi_line_string_token(arg[0])

    def true(self, _: Any) -> Literal[True]:  # noqa: ANN401
        return True

    def false(self, _: Any) -> Literal[False]:  # noqa: ANN401
        return False

    def null(self, _: Any) -> None:  # noqa: ANN401
        return None

    def lambda_expression(self, args: tuple[pycep_typing.PossibleValue, ...]) -> pycep_typing.LambdaExpression:
        arg_1, *arg_x, expr = args

        return {
            "type": "lambda_expression",
            "detail": {
                "var_1": str(arg_1),
                **{f"var_{idx + 2}": str(arg) for idx, arg in enumerate(arg_x)},
                "expression": expr,
            },
        }

    ####################
    #
    # helper methods
    #
    ####################

    def process_child_resource(
        self, parent_resource_name: str, parent_type_api_pair: pycep_typing.ApiTypeVersion, config: dict[str, Any]
    ) -> None:
        """Extracts child resources from a resource config.

        Beware that this method is not idempotent, it modifies the passed in `config`.
        """
        if "__child_resource__" in config:
            child_resource = config.pop("__child_resource__")

            # prefix the resource name with the parent to prevent overlap
            child_resource["__name__"] = f"{parent_resource_name}__{child_resource['__name__']}"

            # inherit type and api version info from parent resource
            child_type_api_pair: pycep_typing.ApiTypeVersion = {
                "type": f"{parent_type_api_pair['type']}/{child_resource['__attrs__']['type']}",
                "api_version": parent_type_api_pair["api_version"],
            }

            child_resource["__attrs__"]["type"] = child_type_api_pair["type"]
            child_resource["__attrs__"]["api_version"] = child_type_api_pair["api_version"]
            child_resource["__attrs__"]["config"].setdefault("depends_on", []).append(
                BicepElement(parent_resource_name)
            )

            self.child_resources.append(
                {
                    "resources": child_resource,
                }
            )

            self.process_child_resource(
                parent_resource_name=child_resource["__name__"],
                parent_type_api_pair=child_type_api_pair,
                config=child_resource["__attrs__"]["config"],
            )
