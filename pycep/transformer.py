from __future__ import annotations

import itertools
import re
from typing import Any, cast

from lark import Token, Transformer, v_args
from lark.tree import Meta
from typing_extensions import Literal

from pycep import typing as pycep_typing

BICEP_REGISTRY_PATTERN = re.compile(r"br:(?P<registry_name>\w+)\.azurecr\.io/(?P<path>[\w/]+):(?P<tag>[\w.\-]+)")
TEMPLATE_SPEC_PATTERN = re.compile(
    r"ts:(?P<sub_id>[\d\-]+)/(?P<rg_id>[\w._\-()]+)/(?P<name>[\w.\-]+):(?P<version>[\w.\-]+)"
)

VALID_TARGET_SCOPES = {"resourceGroup", "subscription", "managementGroup", "tenant"}


class BicepToJson(Transformer[pycep_typing.BicepJson]):
    def __init__(self, add_line_numbers: bool) -> None:
        self.add_line_numbers = add_line_numbers

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

        for arg in itertools.chain(args, self.child_resources):
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
    def param(
        self, meta: Meta, args: tuple[list[pycep_typing.Decorator] | None, str, str, pycep_typing.PossibleNoneValue]
    ) -> pycep_typing.ParamResponse:
        decorators, name, data_type, default = args

        result: pycep_typing.ParamResponse = {
            "parameters": {
                "__name__": str(name),
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
                "__name__": str(name),
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
                    "decorators": decorators if decorators else [],
                    **type_api_pair,  # type: ignore[misc] # https://github.com/python/mypy/issues/11753
                    "existing": True if existing else False,
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
                "existing": True if existing else False,
                "config": config,
            },
        }

        if self.add_line_numbers:
            result["__attrs__"]["__start_line__"] = meta.line
            # remove one line, because the new line is counted for child resources
            result["__attrs__"]["__end_line__"] = meta.end_line - 1

        return ("__child_resource__", result)

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
            if not m:  # pragma: no cover
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
    # functions
    #
    ####################

    def function(self, args: tuple[pycep_typing.Functions]) -> pycep_typing.Function:
        return {"function": args[0]}

    ####################
    #
    # functions - any
    #
    ####################

    def any_func(self, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.AnyFunc:
        return {
            "type": "any",
            "parameters": {
                "value": args[0],
            },
        }

    ####################
    #
    # functions - array
    #
    ####################

    def contains(self, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue]) -> pycep_typing.Contains:
        container, item_to_find = args

        return {
            "type": "contains",
            "parameters": {
                "container": container,
                "item_to_find": item_to_find,
            },
        }

    def empty(self, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.Empty:
        return {
            "type": "empty",
            "parameters": {
                "item_to_test": args[0],
            },
        }

    def intersection(self, args: tuple[str, ...]) -> pycep_typing.Intersection:
        arg_1, arg_2, *arg_x, property_name = args

        result: pycep_typing.Intersection = {
            "type": "intersection",
            "parameters": {
                "arg_1": arg_1,
                "arg_2": arg_2,
                **{f"arg_{idx + 3}": arg for idx, arg in enumerate(arg_x)},  # type: ignore[misc] # dynamic operand creation
            },
        }

        if property_name:
            result["property_name"] = str(property_name)

        return result

    def length(self, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.Length:
        return {
            "type": "length",
            "parameters": {
                "arg_1": args[0],
            },
        }

    def take(self, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue]) -> pycep_typing.Take:
        original_value, number_to_take = args

        return {
            "type": "take",
            "parameters": {
                "original_value": original_value,
                "number_to_take": number_to_take,
            },
        }

    def union(self, args: tuple[str, ...]) -> pycep_typing.UnionFunc:
        arg_1, arg_2, *arg_x, property_name = args

        result: pycep_typing.UnionFunc = {
            "type": "union",
            "parameters": {
                "arg_1": arg_1,
                "arg_2": arg_2,
                **{f"arg_{idx + 3}": arg for idx, arg in enumerate(arg_x)},  # type: ignore[misc] # dynamic operand creation
            },
        }

        if property_name:
            result["property_name"] = str(property_name)

        return result

    ####################
    #
    # functions - date
    #
    ####################

    def date_time_add(
        self, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue, pycep_typing.PossibleNoneValue]
    ) -> pycep_typing.DateTimeAdd:
        base, duration, format_str = args

        return {
            "type": "date_time_add",
            "parameters": {
                "base": base,
                "duration": duration,
                "format": format_str,
            },
        }

    def utc_now(self, args: tuple[pycep_typing.PossibleNoneValue]) -> pycep_typing.UtcNow:
        return {
            "type": "utc_now",
            "parameters": {
                "format": args[0],
            },
        }

    ####################
    #
    # functions - object
    #
    ####################

    def json_func(self, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.Json:
        return {
            "type": "json",
            "parameters": {
                "arg_1": args[0],
            },
        }

    ####################
    #
    # functions - resource
    #
    ####################

    def extension_resource_id(self, args: list[Token]) -> pycep_typing.ExtensionResourceId:
        args_len = len(args)
        if args_len == 3:
            resource_id = str(args[0])
            resource_type = str(args[1])
            resource_name_1 = str(args[2])
            resource_name_2 = None
        else:
            resource_id = str(args[0])
            resource_type = str(args[1])
            resource_name_1 = str(args[2])
            resource_name_2 = str(args[3])

        return {
            "type": "extension_resource_id",
            "parameters": {
                "resource_id": resource_id,
                "resource_type": resource_type,
                "resource_name_1": resource_name_1,
                "resource_name_2": resource_name_2,
            },
        }

    def list_keys(
        self, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue, pycep_typing.PossibleNoneValue]
    ) -> pycep_typing.ListKeys:
        resource_identifier, api_version, property_name = args

        result: pycep_typing.ListKeys = {
            "type": "list_keys",
            "parameters": {
                "resource_identifier": resource_identifier,
                "api_version": api_version,
            },
        }

        if property_name:
            result["property_name"] = str(property_name)

        return result

    def reference(
        self,
        args: tuple[
            pycep_typing.PossibleValue,
            pycep_typing.PossibleNoneValue,
            pycep_typing.PossibleNoneValue,
            pycep_typing.PossibleNoneValue,
        ],
    ) -> pycep_typing.Reference:
        resource_identifier, api_version, full, property_name = args

        result: pycep_typing.Reference = {
            "type": "reference",
            "parameters": {
                "resource_identifier": resource_identifier,
                "api_version": api_version,
                "full": full,
            },
        }

        if property_name:
            result["property_name"] = str(property_name)

        return result

    def resource_id(self, args: list[Token]) -> pycep_typing.ResourceId:
        # args has between 2-5 items and only for the 2 and 5 items case
        # it is possible to determine the correct parameter references
        args_len = len(args)
        if args_len == 2:
            subscription_id = None
            resource_group_name = None
            resource_type = str(args[0])
            resource_name_1 = str(args[1])
            resource_name_2 = None
        elif args_len == 3:
            # this case is ambiguous and it could be any of
            # 0 -> resource_type, 1 -> resource_name_1, 2 -> resource_name_2
            # 0 -> resource_group_name, 1 -> resource_type, 2 -> resource_name_1
            subscription_id = None
            resource_group_name = None
            resource_type = str(args[0])
            resource_name_1 = str(args[1])
            resource_name_2 = str(args[2])
        elif args_len == 4:
            # this case is ambiguous and it could be any of
            # 0 -> resource_group_name, 1 -> resource_type, 2 -> resource_name_1, 3 -> resource_name_2
            # 0 -> subscription_id, 1 -> resource_group_name, 2 -> resource_type, 3 -> resource_name_1
            subscription_id = None
            resource_group_name = str(args[0])
            resource_type = str(args[1])
            resource_name_1 = str(args[2])
            resource_name_2 = str(args[3])
        else:
            subscription_id = str(args[0])
            resource_group_name = str(args[1])
            resource_type = str(args[2])
            resource_name_1 = str(args[3])
            resource_name_2 = str(args[4])

        return {
            "type": "resource_id",
            "parameters": {
                "resource_type": resource_type,
                "resource_name_1": resource_name_1,
                "resource_name_2": resource_name_2,
                "resource_group_name": resource_group_name,
                "subscription_id": subscription_id,
            },
        }

    def subscription_resource_id(self, args: list[Token]) -> pycep_typing.SubscriptionResourceId:
        # args has between 2-4 items and only for the 2 and 4 items case
        # it is possible to determine the correct parameter references
        args_len = len(args)
        if args_len == 2:
            subscription_id = None
            resource_type = str(args[0])
            resource_name_1 = str(args[1])
            resource_name_2 = None
        elif args_len == 3:
            # this case is ambiguous and it could be any of
            # 0 -> resource_type, 1 -> resource_name_1, 2 -> resource_name_2
            # 0 -> subscription_id, 1 -> resource_type, 2 -> resource_name_1
            subscription_id = None
            resource_type = str(args[0])
            resource_name_1 = str(args[1])
            resource_name_2 = str(args[2])
        else:
            subscription_id = str(args[0])
            resource_type = str(args[1])
            resource_name_1 = str(args[2])
            resource_name_2 = str(args[3])

        return {
            "type": "subscription_resource_id",
            "parameters": {
                "resource_type": resource_type,
                "resource_name_1": resource_name_1,
                "resource_name_2": resource_name_2,
                "subscription_id": subscription_id,
            },
        }

    def tenant_resource_id(self, args: list[Token]) -> pycep_typing.TenantResourceId:
        args_len = len(args)
        if args_len == 2:
            resource_type = str(args[0])
            resource_name_1 = str(args[1])
            resource_name_2 = None
        else:
            resource_type = str(args[0])
            resource_name_1 = str(args[1])
            resource_name_2 = str(args[2])

        return {
            "type": "tenant_resource_id",
            "parameters": {
                "resource_type": resource_type,
                "resource_name_1": resource_name_1,
                "resource_name_2": resource_name_2,
            },
        }

    ####################
    #
    # functions - scope
    #
    ####################

    def resource_group(self, args: tuple[Token | None, Token | None, Token | None]) -> pycep_typing.ResourceGroup:
        resource_group_name, subscription_id, property_name = args

        if resource_group_name and subscription_id:
            # very strange parameter definition
            resource_group_name, subscription_id = subscription_id, resource_group_name

        result: pycep_typing.ResourceGroup = {
            "type": "resource_group",
            "parameters": {
                "resource_group_name": str(resource_group_name) if resource_group_name else None,
                "subscription_id": str(subscription_id) if subscription_id else None,
            },
        }

        if property_name:
            result["property_name"] = str(property_name)

        return result

    def subscription(self, args: tuple[Token | None, Token | None]) -> pycep_typing.Subscription:
        subscription_id, property_name = args

        result: pycep_typing.Subscription = {
            "type": "subscription",
            "parameters": {
                "subscription_id": str(subscription_id) if subscription_id else None,
            },
        }

        if property_name:
            result["property_name"] = str(property_name)

        return result

    ####################
    #
    # functions - string
    #
    ####################

    def base64_func(self, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.Base64:
        return {
            "type": "base64",
            "parameters": {
                "input_string": args[0],
            },
        }

    def base64_to_json(self, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.Base64ToJson:
        return {
            "type": "base64_to_json",
            "parameters": {
                "base64_value": args[0],
            },
        }

    def base64_to_string(self, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.Base64ToString:
        return {
            "type": "base64_to_string",
            "parameters": {
                "base64_value": args[0],
            },
        }

    def format(self, args: tuple[pycep_typing.PossibleValue, ...]) -> pycep_typing.Format:
        format_string, *arg_x = args

        return {
            "type": "format",
            "parameters": {
                "format_string": format_string,
                **{f"arg_{idx + 1}": extra for idx, extra in enumerate(arg_x)},  # type: ignore[misc] # dynamic operand creation
            },
        }

    def guid(self, args: tuple[pycep_typing.PossibleValue, ...]) -> pycep_typing.Guid:
        base_string, *extra_string_x = args

        return {
            "type": "guid",
            "parameters": {
                "base_string": base_string,
                **{f"extra_string_{idx + 1}": extra for idx, extra in enumerate(extra_string_x)},  # type: ignore[misc] # dynamic operand creation
            },
        }

    def index_of(self, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue]) -> pycep_typing.IndexOf:
        string_to_search, string_to_find = args

        return {
            "type": "index_of",
            "parameters": {
                "string_to_search": string_to_search,
                "string_to_find": string_to_find,
            },
        }

    def last_index_of(
        self, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue]
    ) -> pycep_typing.LastIndexOf:
        string_to_search, string_to_find = args

        return {
            "type": "last_index_of",
            "parameters": {
                "string_to_search": string_to_search,
                "string_to_find": string_to_find,
            },
        }

    def replace(
        self, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue, pycep_typing.PossibleValue]
    ) -> pycep_typing.Replace:
        original_string, old_string, new_string = args

        return {
            "type": "replace",
            "parameters": {
                "original_string": original_string,
                "old_string": old_string,
                "new_string": new_string,
            },
        }

    def split(self, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue]) -> pycep_typing.Split:
        input_string, delimiter = args

        return {
            "type": "split",
            "parameters": {
                "input_string": input_string,
                "delimiter": delimiter,
            },
        }

    def string_func(self, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.String:
        return {
            "type": "string",
            "parameters": {
                "value_to_convert": args[0],
            },
        }

    def substring(
        self, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue, pycep_typing.PossibleValue]
    ) -> pycep_typing.Substring:
        string_to_parse, start_index, length = args

        return {
            "type": "substring",
            "parameters": {
                "string_to_parse": string_to_parse,
                "start_index": start_index,
                "length": length,
            },
        }

    def to_lower(self, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.ToLower:
        return {
            "type": "to_lower",
            "parameters": {
                "string_to_change": args[0],
            },
        }

    def to_upper(self, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.ToUpper:
        return {
            "type": "to_upper",
            "parameters": {
                "string_to_change": args[0],
            },
        }

    def unique_string(self, args: tuple[pycep_typing.PossibleValue, ...]) -> pycep_typing.UniqueString:
        base_string, *extra_string_x = args

        return {
            "type": "unique_string",
            "parameters": {
                "base_string": base_string,
                **{f"extra_string_{idx + 1}": extra for idx, extra in enumerate(extra_string_x)},  # type: ignore[misc] # dynamic operand creation
            },
        }

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
                **{f"operand_{idx + 3}": op for idx, op in enumerate(operand_x)},  # type: ignore[misc] # dynamic operand creation
            },
        }

    def or_op(self, args: tuple[bool | str, ...]) -> pycep_typing.Or:
        operand_1, operand_2, *operand_x = args

        return {
            "type": "or",
            "operands": {
                "operand_1": operand_1,
                "operand_2": operand_2,
                **{f"operand_{idx + 3}": op for idx, op in enumerate(operand_x)},  # type: ignore[misc] # dynamic operand creation
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
                **{f"operand_{idx + 3}": op for idx, op in enumerate(operand_x)},  # type: ignore[misc] # dynamic operand creation
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

    def minus(self, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.Minus:
        return {
            "type": "minus",
            "operands": {
                "integer_value": args[0],
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

    def null(self, _: Any) -> None:
        return None

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
        if "__child_resource__" in config.keys():
            child_resource = config.pop("__child_resource__")

            # inherit type and api version info from parent resource
            child_type_api_pair: pycep_typing.ApiTypeVersion = {
                "type": f"{parent_type_api_pair['type']}/{child_resource['__attrs__']['type']}",
                "api_version": parent_type_api_pair["api_version"],
            }

            child_resource["__attrs__"]["type"] = child_type_api_pair["type"]
            child_resource["__attrs__"]["api_version"] = child_type_api_pair["api_version"]
            child_resource["__attrs__"].setdefault("depends_on", []).append(parent_resource_name)

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
