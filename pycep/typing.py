from __future__ import annotations

from typing import Any, Dict

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict

# dict[str, Any] -> dict[str, PossibleValue] not supported https://github.com/python/mypy/issues/731
PossibleValue: TypeAlias = "bool | int | str | list[bool | int | str] | dict[str, Any]"
ModulePath: TypeAlias = "LocalModulePath | BicepRegistryModulePath | TemplateSpecModulePath"
LoopType: TypeAlias = "LoopIndex | LoopArray | LoopArrayIndex | LoopObject"
ElementResponse: TypeAlias = "ParamResponse | VarResponse | ResourceResponse | ModuleResponse | OutputResponse"
Decorator: TypeAlias = "DecoratorAllowed | DecoratorBatchSize | DecoratorDescription | DecoratorMinLength | DecoratorMaxLength | DecoratorMinValue | DecoratorMaxValue | DecoratorMetadata | DecoratorSecure"  # noqa: E501, B950
Operators: TypeAlias = "Equals | NotEquals | Conditional"


####################
#
# Elements
#
####################


class _GlobalsAttributes(TypedDict):
    scope: _ScopeAttributes


class Globals(TypedDict):
    globals: _GlobalsAttributes


class _ScopeAttributes(TypedDict):
    value: Literal["resourceGroup", "subscription", "managementGroup", "tenant"]
    __start_line__: NotRequired[int]
    __end_line__: NotRequired[int]


class _Scope(TypedDict):
    __name__: Literal["scope"]
    __attrs__: _ScopeAttributes


class ScopeResponse(TypedDict):
    globals: _Scope


class _ParameterAttributes(TypedDict):
    decorators: list[Decorator]
    type: str
    default: PossibleValue | None
    __start_line__: NotRequired[int]
    __end_line__: NotRequired[int]


class _Parameters(TypedDict):
    __name__: str
    __attrs__: _ParameterAttributes


class ParamResponse(TypedDict):
    parameters: _Parameters


class _VariableAttributes(TypedDict):
    value: PossibleValue
    __start_line__: NotRequired[int]
    __end_line__: NotRequired[int]


class _Variables(TypedDict):
    __name__: str
    __attrs__: _VariableAttributes


class VarResponse(TypedDict):
    variables: _Variables


class _OutputAttributes(TypedDict):
    type: str
    value: PossibleValue
    __start_line__: NotRequired[int]
    __end_line__: NotRequired[int]


class _Outputs(TypedDict):
    __name__: str
    __attrs__: _OutputAttributes


class OutputResponse(TypedDict):
    outputs: _Outputs


class _ResourceAttributes(TypedDict):
    decorators: list[Decorator]
    type: str
    api_version: str
    config: Dict[str, Any]
    __start_line__: NotRequired[int]
    __end_line__: NotRequired[int]


class _Resources(TypedDict):
    __name__: str
    __attrs__: _ResourceAttributes


class ResourceResponse(TypedDict):
    resources: _Resources


class _ModuleAttributes(TypedDict):
    decorators: list[Decorator]
    type: Literal["local"] | Literal["bicep_registry"] | Literal["template_spec"]
    detail: _LocalModulePathDetail | _BicepRegistryModulePathDetail | _TemplateSpecModulePathDetail
    config: Dict[str, Any]
    __start_line__: NotRequired[int]
    __end_line__: NotRequired[int]


class _Modules(TypedDict):
    __name__: str
    __attrs__: _ModuleAttributes


class ModuleResponse(TypedDict):
    modules: _Modules


class ApiTypeVersion(TypedDict):
    type: str
    api_version: str


####################
#
# Module Paths
#
####################


class _LocalModulePathDetail(TypedDict):
    full: str
    path: str


class LocalModulePath(TypedDict):
    type: Literal["local"]
    detail: _LocalModulePathDetail


class _BicepRegistryModulePathDetail(TypedDict):
    full: str
    registry_name: str
    path: str
    tag: str


class BicepRegistryModulePath(TypedDict):
    type: Literal["bicep_registry"]
    detail: _BicepRegistryModulePathDetail


class _TemplateSpecModulePathDetail(TypedDict):
    full: str
    subscription_id: str
    resource_group_id: str
    name: str
    version: str


class TemplateSpecModulePath(TypedDict):
    type: Literal["template_spec"]
    detail: _TemplateSpecModulePathDetail


####################
#
# Loops
#
####################


class _LoopIndexDetail(TypedDict):
    index_name: str
    start_index: str
    count: str


class LoopIndex(TypedDict):
    type: Literal["index"]
    detail: _LoopIndexDetail


class _LoopArrayDetail(TypedDict):
    item_name: str
    array_name: str


class LoopArray(TypedDict):
    type: Literal["array"]
    detail: _LoopArrayDetail


class _LoopArrayIndexDetail(TypedDict):
    item_name: str
    index_name: str
    array_name: str


class LoopArrayIndex(TypedDict):
    type: Literal["array_index"]
    detail: _LoopArrayIndexDetail


class _LoopObjectDetail(TypedDict):
    item_name: str
    object_name: str


class LoopObject(TypedDict):
    type: Literal["object"]
    detail: _LoopObjectDetail


class Loop(TypedDict):
    loop_type: LoopType
    condition: str | None
    config: dict[str, Any]


####################
#
# Decorators
#
####################


class DecoratorAllowed(TypedDict):
    type: Literal["allowed"]
    argument: list[int | str]


class DecoratorBatchSize(TypedDict):
    type: Literal["batchSize"]
    argument: int


class DecoratorDescription(TypedDict):
    type: Literal["description"]
    argument: str


class DecoratorMinLength(TypedDict):
    type: Literal["min_length"]
    argument: int


class DecoratorMaxLength(TypedDict):
    type: Literal["max_length"]
    argument: int


class DecoratorMinValue(TypedDict):
    type: Literal["min_value"]
    argument: int


class DecoratorMaxValue(TypedDict):
    type: Literal["max_value"]
    argument: int


class DecoratorMetadata(TypedDict):
    type: Literal["metadata"]
    argument: dict[str, Any]


class DecoratorSecure(TypedDict):
    type: Literal["secure"]


####################
#
# Operators
#
####################


class _EqualsOperands(TypedDict):
    operand_1: PossibleValue
    operand_2: PossibleValue


class Equals(TypedDict):
    type: Literal["equals"]
    operands: _EqualsOperands


class NotEquals(TypedDict):
    type: Literal["not_equals"]
    operands: _EqualsOperands


class _ConditionalOperands(TypedDict):
    condition: str
    true_value: PossibleValue
    false_value: PossibleValue


class Conditional(TypedDict):
    type: Literal["conditional"]
    operands: _ConditionalOperands


class Operator(TypedDict):
    operator: Operators


####################
#
# JSON response
#
####################


class BicepJson(TypedDict):
    globals: _GlobalsAttributes
    parameters: NotRequired[dict[str, _ParameterAttributes]]
    variables: NotRequired[dict[str, _VariableAttributes]]
    resources: NotRequired[dict[str, _ResourceAttributes]]
    modules: NotRequired[dict[str, _ModuleAttributes]]
    outputs: NotRequired[dict[str, _OutputAttributes]]
