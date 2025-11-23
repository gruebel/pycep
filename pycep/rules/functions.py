from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast

if TYPE_CHECKING:
    from collections.abc import Callable

    from lark import Token

    from pycep import typing as pycep_typing


####################
#
# functions - any
#
####################


def any_func(_func_name: str, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.AnyFunc:
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


def array_func(_func_name: str, args: tuple[pycep_typing.PossibleValue, ...]) -> pycep_typing.Array:
    return {
        "type": "array",
        "parameters": {
            "convert_to_array": args[0],
        },
    }


def concat(_func_name: str, args: tuple[pycep_typing.PossibleValue, ...]) -> pycep_typing.Concat:
    arg_1, *arg_x = args

    return {
        "type": "concat",
        "parameters": {
            "arg_1": arg_1,
            **{f"arg_{idx + 2}": arg for idx, arg in enumerate(arg_x)},  # type: ignore[typeddict-item] # dynamic operand creation
        },
    }


def contains(
    _func_name: str, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue]
) -> pycep_typing.Contains:
    container, item_to_find = args

    return {
        "type": "contains",
        "parameters": {
            "container": container,
            "item_to_find": item_to_find,
        },
    }


def empty(_func_name: str, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.Empty:
    return {
        "type": "empty",
        "parameters": {
            "item_to_test": args[0],
        },
    }


def first(_func_name: str, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.First:
    return {
        "type": "first",
        "parameters": {
            "arg_1": args[0],
        },
    }


def flatten(_func_name: str, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.Flatten:
    return {
        "type": "flatten",
        "parameters": {
            "array_to_flattern": args[0],
        },
    }


def intersection(_func_name: str, args: tuple[str, ...]) -> pycep_typing.Intersection:
    arg_1, arg_2, *arg_x = args

    result: pycep_typing.Intersection = {
        "type": "intersection",
        "parameters": {
            "arg_1": arg_1,
            "arg_2": arg_2,
            **{f"arg_{idx + 3}": arg for idx, arg in enumerate(arg_x)},  # type: ignore[typeddict-item] # dynamic operand creation
        },
    }

    return result


def last(_func_name: str, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.Last:
    return {
        "type": "last",
        "parameters": {
            "arg_1": args[0],
        },
    }


def length(_func_name: str, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.Length:
    return {
        "type": "length",
        "parameters": {
            "arg_1": args[0],
        },
    }


def max_func(_func_name: str, args: tuple[pycep_typing.PossibleValue, ...]) -> pycep_typing.Max:
    arg_1, *arg_x = args

    return {
        "type": "max",
        "parameters": {
            "arg_1": arg_1,
            **{f"arg_{idx + 2}": arg for idx, arg in enumerate(arg_x)},  # type: ignore[typeddict-item] # dynamic operand creation
        },
    }


def min_func(_func_name: str, args: tuple[pycep_typing.PossibleValue, ...]) -> pycep_typing.Min:
    arg_1, *arg_x = args

    return {
        "type": "min",
        "parameters": {
            "arg_1": arg_1,
            **{f"arg_{idx + 2}": arg for idx, arg in enumerate(arg_x)},  # type: ignore[typeddict-item] # dynamic operand creation
        },
    }


def range_func(
    _func_name: str, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue]
) -> pycep_typing.Range:
    start_idx, count = args

    return {
        "type": "range",
        "parameters": {"start_index": start_idx, "count": count},
    }


def skip(_func_name: str, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue]) -> pycep_typing.Skip:
    original_value, number_to_skip = args

    return {
        "type": "skip",
        "parameters": {
            "original_value": original_value,
            "number_to_skip": number_to_skip,
        },
    }


def take(_func_name: str, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue]) -> pycep_typing.Take:
    original_value, number_to_take = args

    return {
        "type": "take",
        "parameters": {
            "original_value": original_value,
            "number_to_take": number_to_take,
        },
    }


def union(_func_name: str, args: tuple[str, ...]) -> pycep_typing.UnionFunc:
    arg_1, arg_2, *arg_x = args

    result: pycep_typing.UnionFunc = {
        "type": "union",
        "parameters": {
            "arg_1": arg_1,
            "arg_2": arg_2,
            **{f"arg_{idx + 3}": arg for idx, arg in enumerate(arg_x)},  # type: ignore[typeddict-item] # dynamic operand creation
        },
    }

    return result


####################
#
# functions - date
#
####################


def date_time_add(
    _func_name: str, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue, pycep_typing.PossibleNoneValue]
) -> pycep_typing.DateTimeAdd:
    base, duration, *format_str = args

    return {
        "type": "date_time_add",
        "parameters": {
            "base": base,
            "duration": duration,
            "format": format_str[0] if format_str else None,
        },
    }


def date_time_from_epoch(_func_name: str, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.DateTimeFromEpoch:
    return {
        "type": "date_time_from_epoch",
        "parameters": {
            "epoch_time": args[0],
        },
    }


def date_time_to_epoch(_func_name: str, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.DateTimeToEpoch:
    return {
        "type": "date_time_to_epoch",
        "parameters": {
            "date_time": args[0],
        },
    }


def utc_now(_func_name: str, args: tuple[pycep_typing.PossibleNoneValue]) -> pycep_typing.UtcNow:
    return {
        "type": "utc_now",
        "parameters": {
            "format": args[0] if args else None,
        },
    }


####################
#
# functions - deployment
#
####################


def deployment(_func_name: str, _args: tuple[None]) -> pycep_typing.Deployment:
    return {"type": "deployment"}


def environment(_func_name: str, _args: tuple[None]) -> pycep_typing.Environment:
    return {"type": "environment"}


####################
#
# functions - file
#
####################


def load_text_content(
    _func_name: str, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleNoneValue]
) -> pycep_typing.LoadTextContent:
    file_path, *encoding = args

    return {
        "type": "load_text_content",
        "parameters": {
            "file_path": file_path,
            "encoding": encoding[0] if encoding else None,
        },
    }


def load_json_content(
    _func_name: str,
    args: tuple[
        pycep_typing.PossibleValue,
        pycep_typing.PossibleNoneValue,
        pycep_typing.PossibleNoneValue,
    ],
) -> pycep_typing.LoadJsonContent:
    file_path, *arg_x = args

    arg_x_len = len(arg_x)
    if arg_x_len == 2:
        json_path, encoding = arg_x
    elif arg_x_len == 1:
        json_path, encoding = arg_x[0], None
    else:
        json_path, encoding = None, None

    return {
        "type": "load_json_content",
        "parameters": {
            "file_path": file_path,
            "json_path": json_path,
            "encoding": encoding,
        },
    }


def load_yaml_content(
    _func_name: str,
    args: tuple[
        pycep_typing.PossibleValue,
        pycep_typing.PossibleNoneValue,
        pycep_typing.PossibleNoneValue,
    ],
) -> pycep_typing.LoadYamlContent:
    file_path, *arg_x = args

    arg_x_len = len(arg_x)
    if arg_x_len == 2:
        path_filter, encoding = arg_x
    elif arg_x_len == 1:
        path_filter, encoding = arg_x[0], None
    else:
        path_filter, encoding = None, None

    return {
        "type": "load_yaml_content",
        "parameters": {
            "file_path": file_path,
            "path_filter": path_filter,
            "encoding": encoding,
        },
    }


def load_file_as_base64(_func_name: str, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.LoadFileAsBase64:
    return {
        "type": "load_file_as_base64",
        "parameters": {
            "file_path": args[0],
        },
    }


####################
#
# functions - lambda
#
####################


def filter_func(
    _func_name: str, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue]
) -> pycep_typing.Filter:
    input_array, expression = args

    return {
        "type": "filter",
        "parameters": {
            "input_array": input_array,
            "expression": expression,
        },
    }


####################
#
# functions - logical
#
####################


def bool_func(_func_name: str, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.BoolFunc:
    return {
        "type": "bool",
        "parameters": {
            "arg_1": args[0],
        },
    }


####################
#
# functions - numeric
#
####################


def int_func(_func_name: str, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.IntFunc:
    return {
        "type": "int",
        "parameters": {
            "value_to_convert": args[0],
        },
    }


####################
#
# functions - object
#
####################


def json_func(_func_name: str, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.Json:
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


def extension_resource_id(_func_name: str, args: list[Token]) -> pycep_typing.ExtensionResourceId:
    args_len = len(args)
    if args_len == 3:
        resource_id = args[0]
        resource_type = args[1]
        resource_name_1 = args[2]
        resource_name_2 = None
    else:
        resource_id = args[0]
        resource_type = args[1]
        resource_name_1 = args[2]
        resource_name_2 = args[3]

    return {
        "type": "extension_resource_id",
        "parameters": {
            "resource_id": resource_id,
            "resource_type": resource_type,
            "resource_name_1": resource_name_1,
            "resource_name_2": resource_name_2,
        },
    }


def list_func(
    _func_name: str,
    args: tuple[
        pycep_typing.PossibleValue,
        pycep_typing.PossibleValue,
    ],
) -> pycep_typing.ListFunc:
    # See https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-resource#list
    # With Bicep v0.4.X, you call list*() using accessor operator, ex: storageAccount.listKeys()
    resource_identifier, api_version = args

    result: pycep_typing.ListFunc = {
        "type": "list_func",
        "parameters": {
            "func_name": "listKeys",
            "resource_identifier": resource_identifier,
            "api_version": api_version,
        },
    }

    return result


def management_group_resource_id(_func_name: str, args: list[Token]) -> pycep_typing.ManagementGroupResourceId:
    args_len = len(args)
    if args_len == 2:
        resource_type = args[0]
        resource_name_1 = args[1]
        resource_name_2 = None
    else:
        resource_type = args[0]
        resource_name_1 = args[1]
        resource_name_2 = args[2]

    return {
        "type": "management_group_resource_id",
        "parameters": {
            "resource_type": resource_type,
            "resource_name_1": resource_name_1,
            "resource_name_2": resource_name_2,
        },
    }


def pick_zones(_func_name: str, args: list[pycep_typing.PossibleNoneValue]) -> pycep_typing.PickZones:
    args_len = len(args)

    provider_namespace = cast("pycep_typing.PossibleValue", args[0])
    resource_type = cast("pycep_typing.PossibleValue", args[1])
    location = cast("pycep_typing.PossibleValue", args[2])
    number_of_zones = None
    offset = None

    if args_len >= 4:
        number_of_zones = args[3]
        if args_len == 5:
            offset = args[4]

    return {
        "type": "pick_zones",
        "parameters": {
            "provider_namespace": provider_namespace,
            "resource_type": resource_type,
            "location": location,
            "number_of_zones": number_of_zones,
            "offset": offset,
        },
    }


def reference(
    _func_name: str,
    args: tuple[
        pycep_typing.PossibleValue,
        pycep_typing.PossibleNoneValue,
        pycep_typing.PossibleNoneValue,
    ],
) -> pycep_typing.Reference:
    resource_identifier, *arg_x = args

    arg_x_len = len(arg_x)
    if arg_x_len == 2:
        api_version, full = arg_x
    elif arg_x_len == 1:
        api_version, full = arg_x[0], None
    else:
        api_version, full = None, None

    result: pycep_typing.Reference = {
        "type": "reference",
        "parameters": {
            "resource_identifier": resource_identifier,
            "api_version": api_version,
            "full": full,
        },
    }

    return result


def resource_id(_func_name: str, args: list[Token]) -> pycep_typing.ResourceId:
    # args has between 2-5 items and only for the 2 and 5 items case
    # it is possible to determine the correct parameter references
    args_len = len(args)
    if args_len == 2:
        subscription_id = None
        resource_group_name = None
        resource_type = args[0]
        resource_name_1 = args[1]
        resource_name_2 = None
    elif args_len == 3:
        # this case is ambiguous and it could be any of
        # 0 -> resource_type, 1 -> resource_name_1, 2 -> resource_name_2
        # 0 -> resource_group_name, 1 -> resource_type, 2 -> resource_name_1
        subscription_id = None
        resource_group_name = None
        resource_type = args[0]
        resource_name_1 = args[1]
        resource_name_2 = args[2]
    elif args_len == 4:
        # this case is ambiguous and it could be any of
        # 0 -> resource_group_name, 1 -> resource_type, 2 -> resource_name_1, 3 -> resource_name_2
        # 0 -> subscription_id, 1 -> resource_group_name, 2 -> resource_type, 3 -> resource_name_1
        subscription_id = None
        resource_group_name = args[0]
        resource_type = args[1]
        resource_name_1 = args[2]
        resource_name_2 = args[3]
    else:
        # in theory there could be many resource_name parameters, but it is currently limited to 7
        subscription_id = args[0]
        resource_group_name = args[1]
        resource_type = args[2]
        # resource_name_1 = args[3]
        # resource_name_2 = args[4]

        return {
            "type": "resource_id",
            "parameters": {
                "resource_type": resource_type,
                **{  # type: ignore[typeddict-item] # dynamic operand creation
                    f"resource_name_{idx}": resource_name for idx, resource_name in enumerate(args[3:], start=1)
                },
                "resource_group_name": resource_group_name,
                "subscription_id": subscription_id,
            },
        }

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


def subscription_resource_id(_func_name: str, args: list[Token]) -> pycep_typing.SubscriptionResourceId:
    # args has between 2-4 items and only for the 2 and 4 items case
    # it is possible to determine the correct parameter references
    args_len = len(args)
    if args_len == 2:
        subscription_id = None
        resource_type = args[0]
        resource_name_1 = args[1]
        resource_name_2 = None
    elif args_len == 3:
        # this case is ambiguous and it could be any of
        # 0 -> resource_type, 1 -> resource_name_1, 2 -> resource_name_2
        # 0 -> subscription_id, 1 -> resource_type, 2 -> resource_name_1
        subscription_id = None
        resource_type = args[0]
        resource_name_1 = args[1]
        resource_name_2 = args[2]
    else:
        subscription_id = args[0]
        resource_type = args[1]
        resource_name_1 = args[2]
        resource_name_2 = args[3]

    return {
        "type": "subscription_resource_id",
        "parameters": {
            "resource_type": resource_type,
            "resource_name_1": resource_name_1,
            "resource_name_2": resource_name_2,
            "subscription_id": subscription_id,
        },
    }


def tenant_resource_id(_func_name: str, args: list[Token]) -> pycep_typing.TenantResourceId:
    args_len = len(args)
    if args_len == 2:
        resource_type = args[0]
        resource_name_1 = args[1]
        resource_name_2 = None
    else:
        resource_type = args[0]
        resource_name_1 = args[1]
        resource_name_2 = args[2]

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


def management_group(_func_name: str, args: tuple[pycep_typing.PossibleNoneValue]) -> pycep_typing.ManagementGroup:
    return {
        "type": "management_group",
        "parameters": {
            "identifier": args[0] if args else None,
        },
    }


def resource_group(
    _func_name: str, args: tuple[pycep_typing.PossibleNoneValue, pycep_typing.PossibleNoneValue]
) -> pycep_typing.ResourceGroup:
    args_len = len(args)
    if args_len == 2:
        resource_group_name, subscription_id = args
    elif args_len == 1:
        resource_group_name, subscription_id = args[0], None
    else:
        resource_group_name, subscription_id = None, None

    if resource_group_name and subscription_id:
        # very strange parameter definition
        resource_group_name, subscription_id = subscription_id, resource_group_name

    result: pycep_typing.ResourceGroup = {
        "type": "resource_group",
        "parameters": {
            "resource_group_name": resource_group_name,
            "subscription_id": subscription_id,
        },
    }

    return result


def subscription(
    _func_name: str, args: tuple[pycep_typing.PossibleNoneValue, Token | None]
) -> pycep_typing.Subscription:
    return {
        "type": "subscription",
        "parameters": {
            "subscription_id": args[0] if args else None,
        },
    }


def tenant(_func_name: str, _args: tuple[None]) -> pycep_typing.Tenant:
    return {"type": "tenant"}


####################
#
# functions - string
#
####################


def base64_func(_func_name: str, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.Base64:
    return {
        "type": "base64",
        "parameters": {
            "input_string": args[0],
        },
    }


def base64_to_json(_func_name: str, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.Base64ToJson:
    return {
        "type": "base64_to_json",
        "parameters": {
            "base64_value": args[0],
        },
    }


def base64_to_string(_func_name: str, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.Base64ToString:
    return {
        "type": "base64_to_string",
        "parameters": {
            "base64_value": args[0],
        },
    }


def data_uri(_func_name: str, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.DataUri:
    return {
        "type": "data_uri",
        "parameters": {
            "string_to_convert": args[0],
        },
    }


def data_uri_to_string(_func_name: str, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.DataUriToString:
    return {
        "type": "data_uri_to_string",
        "parameters": {
            "data_uri_to_convert": args[0],
        },
    }


def ends_with(
    _func_name: str, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue]
) -> pycep_typing.EndsWith:
    string_to_search, string_to_find = args

    return {
        "type": "ends_with",
        "parameters": {
            "string_to_search": string_to_search,
            "string_to_find": string_to_find,
        },
    }


def format_func(_func_name: str, args: tuple[pycep_typing.PossibleValue, ...]) -> pycep_typing.Format:
    format_string, *arg_x = args

    return {
        "type": "format",
        "parameters": {
            "format_string": format_string,
            **{f"arg_{idx + 1}": extra for idx, extra in enumerate(arg_x)},  # type: ignore[typeddict-item] # dynamic operand creation
        },
    }


def guid(_func_name: str, args: tuple[pycep_typing.PossibleValue, ...]) -> pycep_typing.Guid:
    base_string, *extra_string_x = args

    return {
        "type": "guid",
        "parameters": {
            "base_string": base_string,
            **{f"extra_string_{idx + 1}": extra for idx, extra in enumerate(extra_string_x)},  # type: ignore[typeddict-item] # dynamic operand creation
        },
    }


def index_of(
    _func_name: str, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue]
) -> pycep_typing.IndexOf:
    string_to_search, string_to_find = args

    return {
        "type": "index_of",
        "parameters": {
            "string_to_search": string_to_search,
            "string_to_find": string_to_find,
        },
    }


def last_index_of(
    _func_name: str, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue]
) -> pycep_typing.LastIndexOf:
    string_to_search, string_to_find = args

    return {
        "type": "last_index_of",
        "parameters": {
            "string_to_search": string_to_search,
            "string_to_find": string_to_find,
        },
    }


def new_guid(_func_name: str, _args: tuple[object]) -> pycep_typing.NewGuid:
    return {"type": "new_guid"}


def pad_left(
    _func_name: str, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue, pycep_typing.PossibleNoneValue]
) -> pycep_typing.PadLeft:
    value_to_pad, total_length, *padding_character = args

    return {
        "type": "pad_left",
        "parameters": {
            "value_to_pad": value_to_pad,
            "total_length": total_length,
            "padding_character": padding_character[0] if padding_character else None,
        },
    }


def replace(
    _func_name: str, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue, pycep_typing.PossibleValue]
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


def split(_func_name: str, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue]) -> pycep_typing.Split:
    input_string, delimiter = args

    result: pycep_typing.Split = {
        "type": "split",
        "parameters": {
            "input_string": input_string,
            "delimiter": delimiter,
        },
    }

    return result


def join(_func_name: str, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue]) -> pycep_typing.Join:
    input_array, delimiter = args

    result: pycep_typing.Join = {"type": "join", "parameters": {"input_array": input_array, "delimiter": delimiter}}

    return result


def starts_with(
    _func_name: str, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue]
) -> pycep_typing.StartsWith:
    string_to_search, string_to_find = args

    return {
        "type": "starts_with",
        "parameters": {
            "string_to_search": string_to_search,
            "string_to_find": string_to_find,
        },
    }


def string_func(_func_name: str, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.String:
    return {
        "type": "string",
        "parameters": {
            "value_to_convert": args[0],
        },
    }


def substring(
    _func_name: str, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue, pycep_typing.PossibleNoneValue]
) -> pycep_typing.Substring:
    string_to_parse, start_index, *str_length = args

    return {
        "type": "substring",
        "parameters": {
            "string_to_parse": string_to_parse,
            "start_index": start_index,
            "length": str_length[0] if str_length else None,
        },
    }


def to_lower(_func_name: str, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.ToLower:
    return {
        "type": "to_lower",
        "parameters": {
            "string_to_change": args[0],
        },
    }


def to_upper(_func_name: str, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.ToUpper:
    return {
        "type": "to_upper",
        "parameters": {
            "string_to_change": args[0],
        },
    }


def trim(_func_name: str, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.Trim:
    return {
        "type": "trim",
        "parameters": {
            "string_to_trim": args[0],
        },
    }


def unique_string(_func_name: str, args: tuple[pycep_typing.PossibleValue, ...]) -> pycep_typing.UniqueString:
    base_string, *extra_string_x = args

    return {
        "type": "unique_string",
        "parameters": {
            "base_string": base_string,
            **{f"extra_string_{idx + 1}": extra for idx, extra in enumerate(extra_string_x)},  # type: ignore[typeddict-item] # dynamic operand creation
        },
    }


def uri(_func_name: str, args: tuple[pycep_typing.PossibleValue, pycep_typing.PossibleValue]) -> pycep_typing.Uri:
    base_uri, relative_uri = args

    return {
        "type": "uri",
        "parameters": {
            "base_uri": base_uri,
            "relative_uri": relative_uri,
        },
    }


def uri_component(_func_name: str, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.UriComponent:
    return {
        "type": "uri_component",
        "parameters": {
            "string_to_encode": args[0],
        },
    }


def uri_component_to_string(
    _func_name: str, args: tuple[pycep_typing.PossibleValue]
) -> pycep_typing.UriComponentToString:
    return {
        "type": "uri_component_to_string",
        "parameters": {
            "uri_encoded_string": args[0],
        },
    }


####################
#
# placeholder for unknown built-in and self-defined functions
#
####################


def unknown_func(func_name: str, args: tuple[pycep_typing.PossibleValue, ...]) -> pycep_typing.UnknownFunction:
    return {
        "type": func_name,
        "parameters": {f"arg_{idx + 1}": arg for idx, arg in enumerate(args)},  # type: ignore[typeddict-item] # dynamic operand creation
    }


####################
#
#
#
####################

FUNCTIONS: dict[str, Callable[[str, Any], pycep_typing.Functions]] = {
    # any
    "any": any_func,
    "sys.any": any_func,
    # array
    "array": array_func,
    "sys.array": array_func,
    "concat": concat,
    "sys.concat": concat,
    "contains": contains,
    "sys.contains": contains,
    "empty": empty,
    "sys.empty": empty,
    "first": first,
    "sys.first": first,
    "flatten": flatten,
    "sys.flatten": flatten,
    "intersection": intersection,
    "sys.intersection": intersection,
    "last": last,
    "sys.last": last,
    "length": length,
    "sys.length": length,
    "max": max_func,
    "sys.max": max_func,
    "min": min_func,
    "sys.min": min_func,
    "range": range_func,
    "sys.range": range_func,
    "skip": skip,
    "sys.skip": skip,
    "take": take,
    "sys.take": take,
    "union": union,
    "sys.union": union,
    # date
    "dateTimeAdd": date_time_add,
    "sys.dateTimeAdd": date_time_add,
    "dateTimeFromEpoch": date_time_from_epoch,
    "sys.dateTimeFromEpoch": date_time_from_epoch,
    "dateTimeToEpoch": date_time_to_epoch,
    "sys.dateTimeToEpoch": date_time_to_epoch,
    "utcNow": utc_now,
    "sys.utcNow": utc_now,
    # deployment
    "deployment": deployment,
    "az.deployment": deployment,
    "environment": environment,
    "az.environment": environment,
    # file
    "loadFileAsBase64": load_file_as_base64,
    "sys.loadFileAsBase64": load_file_as_base64,
    "loadJsonContent": load_json_content,
    "sys.loadJsonContent": load_json_content,
    "loadTextContent": load_text_content,
    "sys.loadTextContent": load_text_content,
    "loadYamlContent": load_yaml_content,
    "sys.loadYamlContent": load_yaml_content,
    # lambda
    "filter": filter_func,
    "sys.filter": filter_func,
    # logical
    "bool": bool_func,
    "sys.bool": bool_func,
    # numeric
    "int": int_func,
    "sys.int": int_func,
    # object
    "json": json_func,
    "sys.json": json_func,
    # resource
    "extensionResourceId": extension_resource_id,
    "az.extensionResourceId": extension_resource_id,
    "listKeys": list_func,
    "az.listKeys": list_func,
    "managementGroupResourceId": management_group_resource_id,
    "az.managementGroupResourceId": management_group_resource_id,
    "pickZones": pick_zones,
    "az.pickZones": pick_zones,
    "reference": reference,
    "az.reference": reference,
    "resourceId": resource_id,
    "az.resourceId": resource_id,
    "subscriptionResourceId": subscription_resource_id,
    "az.subscriptionResourceId": subscription_resource_id,
    "tenantResourceId": tenant_resource_id,
    "az.tenantResourceId": tenant_resource_id,
    # scope
    "managementGroup": management_group,
    "az.managementGroup": management_group,
    "resourceGroup": resource_group,
    "az.resourceGroup": resource_group,
    "subscription": subscription,
    "az.subscription": subscription,
    "tenant": tenant,
    "az.tenant": tenant,
    # string
    "base64": base64_func,
    "sys.base64": base64_func,
    "base64ToJson": base64_to_json,
    "sys.base64ToJson": base64_to_json,
    "base64ToString": base64_to_string,
    "sys.base64ToString": base64_to_string,
    "dataUri": data_uri,
    "sys.dataUri": data_uri,
    "dataUriToString": data_uri_to_string,
    "sys.dataUriToString": data_uri_to_string,
    "endsWith": ends_with,
    "sys.endsWith": ends_with,
    "format": format_func,
    "sys.format": format_func,
    "guid": guid,
    "sys.guid": guid,
    "indexOf": index_of,
    "sys.indexOf": index_of,
    "join": join,
    "sys.join": join,
    "lastIndexOf": last_index_of,
    "sys.lastIndexOf": last_index_of,
    "newGuid": new_guid,
    "sys.newGuid": new_guid,
    "padLeft": pad_left,
    "sys.padLeft": pad_left,
    "replace": replace,
    "sys.replace": replace,
    "split": split,
    "sys.split": split,
    "startsWith": starts_with,
    "sys.startsWith": starts_with,
    "string": string_func,
    "sys.string": string_func,
    "substring": substring,
    "sys.substring": substring,
    "toLower": to_lower,
    "sys.toLower": to_lower,
    "toUpper": to_upper,
    "sys.toUpper": to_upper,
    "trim": trim,
    "sys.trim": trim,
    "uniqueString": unique_string,
    "sys.uniqueString": unique_string,
    "uri": uri,
    "sys.uri": uri,
    "uriComponent": uri_component,
    "sys.uriComponent": uri_component,
    "uriComponentToString": uri_component_to_string,
    "sys.uriComponentToString": uri_component_to_string,
}

UNKNOWN_FUNCTION = unknown_func
