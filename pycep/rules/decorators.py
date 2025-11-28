from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Callable

    from lark import Token

    from pycep import typing as pycep_typing

####################
#
# decorators
#
####################


def deco_allowed(_deco_name: str, args: tuple[list[int | str]]) -> pycep_typing.DecoratorAllowed:
    return {
        "type": "allowed",
        "argument": args[0],
    }


def deco_batch(_deco_name: str, args: tuple[int]) -> pycep_typing.DecoratorBatchSize:
    return {
        "type": "batchSize",
        "argument": args[0],
    }


def deco_description(_deco_name: str, args: tuple[str]) -> pycep_typing.DecoratorDescription:
    return {
        "type": "description",
        "argument": args[0],
    }


def deco_export(_deco_name: str, _args: tuple[None]) -> pycep_typing.DecoratorExport:
    return {
        "type": "export",
    }


def deco_min_len(_deco_name: str, args: tuple[int]) -> pycep_typing.DecoratorMinLength:
    return {
        "type": "min_length",
        "argument": args[0],
    }


def deco_max_len(_deco_name: str, args: tuple[int]) -> pycep_typing.DecoratorMaxLength:
    return {
        "type": "max_length",
        "argument": args[0],
    }


def deco_min_val(_deco_name: str, args: tuple[int | dict[str, Any]]) -> pycep_typing.DecoratorMinValue:
    arg = args[0]
    if isinstance(arg, dict) and (operator := arg.get("operator", {})).get("type") == "minus":
        arg = operator["operands"]["integer_value"] * -1

    return {
        "type": "min_value",
        "argument": arg,  # type: ignore[typeddict-item] # there is no real issue, if this returns a dict
    }


def deco_max_val(_deco_name: str, args: tuple[Token]) -> pycep_typing.DecoratorMaxValue:
    return {
        "type": "max_value",
        "argument": int(args[0]),
    }


def deco_metadata(_deco_name: str, args: tuple[dict[str, Any]]) -> pycep_typing.DecoratorMetadata:
    return {
        "type": "metadata",
        "argument": args[0],
    }


def deco_sealed(_deco_name: str, _args: tuple[None]) -> pycep_typing.DecoratorSealed:
    return {
        "type": "sealed",
    }


def deco_secure(_deco_name: str, _args: tuple[None]) -> pycep_typing.DecoratorSecure:
    return {
        "type": "secure",
    }


####################
#
# placeholder for unknown decorators
#
####################


def unknown_deco(deco_name: str, args: tuple[pycep_typing.PossibleValue]) -> pycep_typing.UnknownDecorator:
    result: pycep_typing.UnknownDecorator = {
        "type": deco_name,
    }

    if args:
        result["argument"] = args[0]

    return result


####################
#
# exposed collections
#
####################

DECORATORS: dict[str, Callable[[str, Any], pycep_typing.Decorator]] = {
    "allowed": deco_allowed,
    "sys.allowed": deco_allowed,
    "batchSize": deco_batch,
    "sys.batchSize": deco_batch,
    "description": deco_description,
    "sys.description": deco_description,
    "export": deco_export,
    "sys.export": deco_export,
    "minLength": deco_min_len,
    "sys.minLength": deco_min_len,
    "maxLength": deco_max_len,
    "sys.maxLength": deco_max_len,
    "minValue": deco_min_val,
    "sys.minValue": deco_min_val,
    "maxValue": deco_max_val,
    "sys.maxValue": deco_max_val,
    "metadata": deco_metadata,
    "sys.metadata": deco_metadata,
    "sealed": deco_sealed,
    "sys.sealed": deco_sealed,
    "secure": deco_secure,
    "sys.secure": deco_secure,
}


UNKNOWN_DECORATOR = unknown_deco
