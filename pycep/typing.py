from __future__ import annotations

from typing import Any, Dict

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict

# dict[str, Any] -> dict[str, PossibleValue] not supported https://github.com/python/mypy/issues/731
PossibleValue: TypeAlias = "bool | int | str | list[bool | int | str] | dict[str, Any]"
PossibleNoneValue: TypeAlias = "PossibleValue | None"

ModulePath: TypeAlias = "LocalModulePath | BicepRegistryModulePath | TemplateSpecModulePath"
LoopType: TypeAlias = "LoopIndex | LoopArray | LoopArrayIndex | LoopObject"
ElementResponse: TypeAlias = "ParamResponse | VarResponse | ResourceResponse | ModuleResponse | OutputResponse"
Decorator: TypeAlias = "DecoratorAllowed | DecoratorBatchSize | DecoratorDescription | DecoratorMinLength | DecoratorMaxLength | DecoratorMinValue | DecoratorMaxValue | DecoratorMetadata | DecoratorSecure"

ComparisonOperators: TypeAlias = "GreaterThanOrEquals | GreaterThan | LessThanOrEquals | LessThan | Equals | NotEquals | EqualsCaseInsensitive | NotEqualsCaseInsensitive"
LogicalOperators: TypeAlias = "And | Or | Not | Coalesce | Conditional"
NumericOperators: TypeAlias = "Add | Minus | Substract"
Operators: TypeAlias = "ComparisonOperators | LogicalOperators | NumericOperators"

AnyFunctions: TypeAlias = "AnyFunc"
ArrayFunctions: TypeAlias = "Contains | Empty | Intersection | Length | Take | UnionFunc"
DateFunctions: TypeAlias = "DateTimeAdd | UtcNow"
ObjectFunctions: TypeAlias = "Json"
ResourceFunctions: TypeAlias = (
    "ExtensionResourceId | ListKeys | Reference | ResourceId | SubscriptionResourceId | TenantResourceId"
)
ScopeFunctions: TypeAlias = "ResourceGroup | Subscription"
StringFunctions: TypeAlias = "Base64 | Base64ToJson | Base64ToString | Format | Guid | IndexOf | LastIndexOf | Split | Substring | String | ToLower | ToUpper | UniqueString"
Functions: TypeAlias = "AnyFunctions | ArrayFunctions | DateFunctions | ObjectFunctions | ResourceFunctions | ScopeFunctions | StringFunctions"


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
    default: PossibleNoneValue
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
    existing: bool
    config: Dict[str, Any]
    __start_line__: NotRequired[int]
    __end_line__: NotRequired[int]


class Resource(TypedDict):
    __name__: str
    __attrs__: _ResourceAttributes


class ResourceResponse(TypedDict):
    resources: Resource


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
    condition: PossibleNoneValue
    config: dict[str, Any]


####################
#
# deploy condition
#
####################


class DeployCondition(TypedDict):
    condition: PossibleValue
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
# functions
#
####################


class Function(TypedDict):
    function: Functions


####################
#
# functions - any
#
####################


class _AnyParameters(TypedDict):
    value: PossibleValue


class AnyFunc(TypedDict):
    type: Literal["any"]
    parameters: _AnyParameters


####################
#
# functions - array
#
####################


class _ContainsParameters(TypedDict):
    container: PossibleValue
    item_to_find: PossibleValue


class Contains(TypedDict):
    type: Literal["contains"]
    parameters: _ContainsParameters


class _EmptyParameters(TypedDict):
    item_to_test: PossibleValue


class Empty(TypedDict):
    type: Literal["empty"]
    parameters: _EmptyParameters


class Intersection(TypedDict):
    type: Literal["intersection"]
    parameters: _UnionParameters
    property_name: NotRequired[str]


class _LengthParameters(TypedDict):
    arg_1: PossibleValue


class Length(TypedDict):
    type: Literal["length"]
    parameters: _LengthParameters


class _TakeParameters(TypedDict):
    original_value: PossibleValue
    number_to_take: PossibleValue


class Take(TypedDict):
    type: Literal["take"]
    parameters: _TakeParameters


class _UnionParameters(TypedDict):
    arg_1: str
    arg_2: str
    arg_3: NotRequired[str]  # and many more possible


class UnionFunc(TypedDict):
    type: Literal["union"]
    parameters: _UnionParameters
    property_name: NotRequired[str]


####################
#
# functions - date
#
####################


class _DateTimeAddParameters(TypedDict):
    base: PossibleValue
    duration: PossibleValue
    format: PossibleNoneValue


class DateTimeAdd(TypedDict):
    type: Literal["date_time_add"]
    parameters: _DateTimeAddParameters


class _UtcNowParameters(TypedDict):
    format: PossibleNoneValue


class UtcNow(TypedDict):
    type: Literal["utc_now"]
    parameters: _UtcNowParameters


####################
#
# functions - object
#
####################


class _JsonParameters(TypedDict):
    arg_1: PossibleValue


class Json(TypedDict):
    type: Literal["json"]
    parameters: _JsonParameters


####################
#
# functions - resource
#
####################


class _ExtensionResourceIdParameters(TypedDict):
    resource_id: str
    resource_type: str
    resource_name_1: str
    resource_name_2: str | None


class ExtensionResourceId(TypedDict):
    type: Literal["extension_resource_id"]
    parameters: _ExtensionResourceIdParameters


class _ListKeysParameters(TypedDict):
    resource_identifier: PossibleValue
    api_version: PossibleValue


class ListKeys(TypedDict):
    type: Literal["list_keys"]
    parameters: _ListKeysParameters
    property_name: NotRequired[str]


class _ReferenceParameters(TypedDict):
    resource_identifier: PossibleValue
    api_version: PossibleNoneValue
    full: PossibleNoneValue


class Reference(TypedDict):
    type: Literal["reference"]
    parameters: _ReferenceParameters
    property_name: NotRequired[str]


class _ResourceIdParameters(TypedDict):
    resource_type: str
    resource_name_1: str
    resource_name_2: str | None
    resource_group_name: str | None
    subscription_id: str | None


class ResourceId(TypedDict):
    type: Literal["resource_id"]
    parameters: _ResourceIdParameters


class _SubscriptionResourceIdParameters(TypedDict):
    resource_type: str
    resource_name_1: str
    resource_name_2: str | None
    subscription_id: str | None


class SubscriptionResourceId(TypedDict):
    type: Literal["subscription_resource_id"]
    parameters: _SubscriptionResourceIdParameters


class _TenantResourceIdParameters(TypedDict):
    resource_type: str
    resource_name_1: str
    resource_name_2: str | None


class TenantResourceId(TypedDict):
    type: Literal["tenant_resource_id"]
    parameters: _TenantResourceIdParameters


####################
#
# functions - scope
#
####################


class _ResourceGroupParameters(TypedDict):
    resource_group_name: str | None
    subscription_id: str | None


class ResourceGroup(TypedDict):
    type: Literal["resource_group"]
    parameters: _ResourceGroupParameters
    property_name: NotRequired[str]


class _SubscriptionParameters(TypedDict):
    subscription_id: str | None


class Subscription(TypedDict):
    type: Literal["subscription"]
    parameters: _SubscriptionParameters
    property_name: NotRequired[str]


####################
#
# functions - string
#
####################


class _Base64Parameters(TypedDict):
    input_string: PossibleValue


class Base64(TypedDict):
    type: Literal["base64"]
    parameters: _Base64Parameters


class _Base64ToJsonParameters(TypedDict):
    base64_value: PossibleValue


class Base64ToJson(TypedDict):
    type: Literal["base64_to_json"]
    parameters: _Base64ToJsonParameters


class Base64ToString(TypedDict):
    type: Literal["base64_to_string"]
    parameters: _Base64ToJsonParameters


class _FormatParameters(TypedDict):
    format_string: PossibleValue
    arg_1: PossibleValue
    arg_2: NotRequired[PossibleValue]  # and many more possible


class Format(TypedDict):
    type: Literal["format"]
    parameters: _FormatParameters


class _GuidParameters(TypedDict):
    base_string: str
    extra_string_1: NotRequired[str]  # and many more possible


class Guid(TypedDict):
    type: Literal["guid"]
    parameters: _GuidParameters


class _IndexOfParameters(TypedDict):
    string_to_search: PossibleValue
    string_to_find: PossibleValue


class IndexOf(TypedDict):
    type: Literal["index_of"]
    parameters: _IndexOfParameters


class LastIndexOf(TypedDict):
    type: Literal["last_index_of"]
    parameters: _IndexOfParameters


class _ReplaceParameters(TypedDict):
    original_string: PossibleValue
    old_string: PossibleValue
    new_string: PossibleValue


class Replace(TypedDict):
    type: Literal["replace"]
    parameters: _ReplaceParameters


class _SplitParameters(TypedDict):
    input_string: PossibleValue
    delimiter: PossibleValue


class Split(TypedDict):
    type: Literal["split"]
    parameters: _SplitParameters


class _StringParameters(TypedDict):
    value_to_convert: PossibleValue


class String(TypedDict):
    type: Literal["string"]
    parameters: _StringParameters


class _SubstringParameters(TypedDict):
    string_to_parse: PossibleValue
    start_index: PossibleValue
    length: PossibleValue


class Substring(TypedDict):
    type: Literal["substring"]
    parameters: _SubstringParameters


class _ToLowerParameters(TypedDict):
    string_to_change: PossibleValue


class ToLower(TypedDict):
    type: Literal["to_lower"]
    parameters: _ToLowerParameters


class ToUpper(TypedDict):
    type: Literal["to_upper"]
    parameters: _ToLowerParameters


class UniqueString(TypedDict):
    type: Literal["unique_string"]
    parameters: _GuidParameters


####################
#
# Operators
#
####################


class Operator(TypedDict):
    operator: Operators


####################
#
# Operators - comparison
#
####################


class _EqualsOperands(TypedDict):
    operand_1: PossibleValue
    operand_2: PossibleValue


class GreaterThanOrEquals(TypedDict):
    type: Literal["greater_than_or_equals"]
    operands: _EqualsOperands


class GreaterThan(TypedDict):
    type: Literal["greater_than"]
    operands: _EqualsOperands


class LessThanOrEquals(TypedDict):
    type: Literal["less_than_or_equals"]
    operands: _EqualsOperands


class LessThan(TypedDict):
    type: Literal["less_than"]
    operands: _EqualsOperands


class Equals(TypedDict):
    type: Literal["equals"]
    operands: _EqualsOperands


class NotEquals(TypedDict):
    type: Literal["not_equals"]
    operands: _EqualsOperands


class EqualsCaseInsensitive(TypedDict):
    type: Literal["equals_case_insensitive"]
    operands: _EqualsOperands


class NotEqualsCaseInsensitive(TypedDict):
    type: Literal["not_equals_case_insensitive"]
    operands: _EqualsOperands


####################
#
# Operators - logical
#
####################


class _AndOperands(TypedDict):
    operand_1: PossibleValue
    operand_2: PossibleValue
    operand_3: NotRequired[PossibleValue]  # and many more possible


class And(TypedDict):
    type: Literal["and"]
    operands: _AndOperands


class Or(TypedDict):
    type: Literal["or"]
    operands: _AndOperands


class _NotOperands(TypedDict):
    bool_value: bool | str


class Not(TypedDict):
    type: Literal["not"]
    operands: _NotOperands


class Coalesce(TypedDict):
    type: Literal["coalesce"]
    operands: _AndOperands


class _ConditionalOperands(TypedDict):
    condition: PossibleValue
    true_value: PossibleValue
    false_value: PossibleValue


class Conditional(TypedDict):
    type: Literal["conditional"]
    operands: _ConditionalOperands


####################
#
# Operators - numeric
#
####################


class Add(TypedDict):
    type: Literal["add"]
    operands: _SubstractOperands


class _MinusOperands(TypedDict):
    integer_value: PossibleValue


class Minus(TypedDict):
    type: Literal["minus"]
    operands: _MinusOperands


class _SubstractOperands(TypedDict):
    operand_1: PossibleValue
    operand_2: PossibleValue


class Substract(TypedDict):
    type: Literal["substract"]
    operands: _SubstractOperands


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
