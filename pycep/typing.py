from __future__ import annotations

from typing import Any, Literal, TypedDict

from typing_extensions import NotRequired, TypeAlias

PossibleValue: TypeAlias = "bool | int | str | list[bool | int | str] | dict[str, PossibleValue]"
PossibleNoneValue: TypeAlias = "PossibleValue | None"

ModulePath: TypeAlias = "LocalModulePath | BicepRegistryModulePath | BicepRegistryAliasModulePath | TemplateSpecModulePath | TemplateSpecAliasModulePath"
ModuleDetail: TypeAlias = "_LocalModulePathDetail | _BicepRegistryModulePathDetail | _BicepRegistryAliasModulePathDetail | _TemplateSpecModulePathDetail | _TemplateSpecAliasModulePathDetail"
LoopType: TypeAlias = "LoopArray | LoopArrayIndex | LoopObject | LoopRange"
ElementResponse: TypeAlias = (
    "ParamResponse | VarResponse | ResourceResponse | ModuleResponse | OutputResponse | TypeResponse"
)
Decorator: TypeAlias = "DecoratorAllowed | DecoratorBatchSize | DecoratorDescription | DecoratorMinLength | DecoratorMaxLength | DecoratorMinValue | DecoratorMaxValue | DecoratorMetadata | DecoratorSecure"

ComparisonOperators: TypeAlias = "GreaterThanOrEquals | GreaterThan | LessThanOrEquals | LessThan | Equals | NotEquals | EqualsCaseInsensitive | NotEqualsCaseInsensitive"
LogicalOperators: TypeAlias = "And | Or | Not | Coalesce | Conditional"
NumericOperators: TypeAlias = "Add | Divide | Minus | Modulo | Multiply | Substract"
AccessorOperators: TypeAlias = "IndexAccessor | FunctionAccessor | NestedResourceAccessor | PropertyAccessor"
Operators: TypeAlias = "ComparisonOperators | LogicalOperators | NumericOperators | AccessorOperators"

AnyFunctions: TypeAlias = "AnyFunc"
ArrayFunctions: TypeAlias = "Array | Concat | Contains | Empty | First | Flatten | Intersection | Last | Length | Max | Min | Skip | Take | UnionFunc"
DateFunctions: TypeAlias = "DateTimeAdd | DateTimeFromEpoch | DateTimeToEpoch | UtcNow"
DeploymentFunctions: TypeAlias = "Deployment | Environment"
FileFunctions: TypeAlias = "LoadFileAsBase64 | LoadJsonContent | LoadYamlContent | LoadTextContent"
LambdaFunctions: TypeAlias = "Filter"
LogicalFunctions: TypeAlias = "BoolFunc"
NumericFunctions: TypeAlias = "IntFunc"
ObjectFunctions: TypeAlias = "Json"
ResourceFunctions: TypeAlias = "ExtensionResourceId | ListFunc | ManagementGroupResourceId | PickZones | Reference | ResourceId | SubscriptionResourceId | TenantResourceId"
ScopeFunctions: TypeAlias = "ManagementGroup | ResourceGroup | Subscription | Tenant"
StringFunctions: TypeAlias = "Base64 | Base64ToJson | Base64ToString | DataUri | DataUriToString | EndsWith | Format | Guid | IndexOf | LastIndexOf | NewGuid | Split | Join | StartsWith | String | Substring | ToLower | ToUpper | Trim | UniqueString | Uri | UriComponent | UriComponentToString"
Functions: TypeAlias = "AnyFunctions | ArrayFunctions | DateFunctions | DeploymentFunctions | FileFunctions | LambdaFunctions | LogicalFunctions | NumericFunctions | ObjectFunctions | ResourceFunctions | ScopeFunctions | StringFunctions"


####################
#
# Elements
#
####################


class GlobalsAttributes(TypedDict):
    scope: ScopeAttributes


class Globals(TypedDict):
    globals: GlobalsAttributes


class ScopeAttributes(TypedDict):
    value: Literal["resourceGroup", "subscription", "managementGroup", "tenant"]
    __start_line__: NotRequired[int]
    __end_line__: NotRequired[int]


class _Scope(TypedDict):
    __name__: Literal["scope"]
    __attrs__: ScopeAttributes


class ScopeResponse(TypedDict):
    globals: _Scope


class MetadataAttributes(TypedDict):
    value: str
    __start_line__: NotRequired[int]
    __end_line__: NotRequired[int]


class _Metadata(TypedDict):
    __name__: str
    __attrs__: MetadataAttributes


class MetadataResponse(TypedDict):
    metadata: _Metadata


class ParameterAttributes(TypedDict):
    decorators: list[Decorator]
    type: str
    default: PossibleNoneValue
    __start_line__: NotRequired[int]
    __end_line__: NotRequired[int]


class _Parameters(TypedDict):
    __name__: str
    __attrs__: ParameterAttributes


class ParamResponse(TypedDict):
    parameters: _Parameters


class VariableAttributes(TypedDict):
    decorators: list[Decorator]
    value: PossibleValue
    __start_line__: NotRequired[int]
    __end_line__: NotRequired[int]


class _Variables(TypedDict):
    __name__: str
    __attrs__: VariableAttributes


class VarResponse(TypedDict):
    variables: _Variables


class OutputAttributes(TypedDict):
    decorators: list[Decorator]
    type: str
    value: PossibleValue
    __start_line__: NotRequired[int]
    __end_line__: NotRequired[int]


class _Outputs(TypedDict):
    __name__: str
    __attrs__: OutputAttributes


class OutputResponse(TypedDict):
    outputs: _Outputs


class ResourceAttributes(TypedDict):
    decorators: list[Decorator]
    type: str
    api_version: str
    existing: bool
    config: dict[str, Any]
    __start_line__: NotRequired[int]
    __end_line__: NotRequired[int]


class Resource(TypedDict):
    __name__: str
    __attrs__: ResourceAttributes


class ResourceResponse(TypedDict):
    resources: Resource


class ModuleAttributes(TypedDict):
    decorators: list[Decorator]
    type: Literal["local", "bicep_registry", "bicep_registry_alias", "template_spec", "template_spec_alias"]
    detail: ModuleDetail
    config: dict[str, Any]
    __start_line__: NotRequired[int]
    __end_line__: NotRequired[int]


class _Modules(TypedDict):
    __name__: str
    __attrs__: ModuleAttributes


class ModuleResponse(TypedDict):
    modules: _Modules


class ApiTypeVersion(TypedDict):
    type: str
    api_version: str


class TypeResponse(TypedDict):
    types: _Variables


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
    public: bool


class BicepRegistryModulePath(TypedDict):
    type: Literal["bicep_registry"]
    detail: _BicepRegistryModulePathDetail


class _BicepRegistryAliasModulePathDetail(TypedDict):
    full: str
    alias: str
    path: str
    tag: str
    public: bool


class BicepRegistryAliasModulePath(TypedDict):
    type: Literal["bicep_registry_alias"]
    detail: _BicepRegistryAliasModulePathDetail


class _TemplateSpecModulePathDetail(TypedDict):
    full: str
    subscription_id: str
    resource_group_id: str
    name: str
    version: str


class TemplateSpecModulePath(TypedDict):
    type: Literal["template_spec"]
    detail: _TemplateSpecModulePathDetail


class _TemplateSpecAliasModulePathDetail(TypedDict):
    full: str
    alias: str
    path: str
    tag: str


class TemplateSpecAliasModulePath(TypedDict):
    type: Literal["template_spec_alias"]
    detail: _TemplateSpecAliasModulePathDetail


####################
#
# Loops
#
####################


class _LoopRangeDetail(TypedDict):
    item_name: str | None
    index_name: str
    start_index: PossibleValue
    count: PossibleValue


class LoopRange(TypedDict):
    type: Literal["range"]
    detail: _LoopRangeDetail


class _LoopArrayDetail(TypedDict):
    item_name: str
    array_name: PossibleValue


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


class _ArrayParameters(TypedDict):
    convert_to_array: PossibleValue


class Array(TypedDict):
    type: Literal["array"]
    parameters: _ArrayParameters


class Concat(TypedDict):
    type: Literal["concat"]
    parameters: _UnionParameters


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


class First(TypedDict):
    type: Literal["first"]
    parameters: _LengthParameters
    property_name: NotRequired[str]


class _FlattenParameters(TypedDict):
    array_to_flattern: PossibleValue


class Flatten(TypedDict):
    type: Literal["flatten"]
    parameters: _FlattenParameters
    property_name: NotRequired[str]


class Intersection(TypedDict):
    type: Literal["intersection"]
    parameters: _UnionParameters
    property_name: NotRequired[str]


class Last(TypedDict):
    type: Literal["last"]
    parameters: _LengthParameters
    property_name: NotRequired[str]


class _LengthParameters(TypedDict):
    arg_1: PossibleValue


class Length(TypedDict):
    type: Literal["length"]
    parameters: _LengthParameters


class Max(TypedDict):
    type: Literal["max"]
    parameters: _UnionParameters


class Min(TypedDict):
    type: Literal["min"]
    parameters: _UnionParameters


class _SkipParameters(TypedDict):
    original_value: PossibleValue
    number_to_skip: PossibleValue


class Skip(TypedDict):
    type: Literal["skip"]
    parameters: _SkipParameters


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


class _DateTimeFromEpochParameters(TypedDict):
    epoch_time: PossibleValue


class DateTimeFromEpoch(TypedDict):
    type: Literal["date_time_from_epoch"]
    parameters: _DateTimeFromEpochParameters


class _DateTimeToEpochParameters(TypedDict):
    date_time: PossibleValue


class DateTimeToEpoch(TypedDict):
    type: Literal["date_time_to_epoch"]
    parameters: _DateTimeToEpochParameters


class _UtcNowParameters(TypedDict):
    format: PossibleNoneValue


class UtcNow(TypedDict):
    type: Literal["utc_now"]
    parameters: _UtcNowParameters


####################
#
# functions - deployment
#
####################


class Deployment(TypedDict):
    type: Literal["deployment"]
    property_name: NotRequired[str]


class Environment(TypedDict):
    type: Literal["environment"]
    property_name: NotRequired[str]


####################
#
# functions - file
#
####################


class _LoadFileAsBase64Parameters(TypedDict):
    file_path: PossibleValue


class LoadFileAsBase64(TypedDict):
    type: Literal["load_file_as_base64"]
    parameters: _LoadFileAsBase64Parameters


class _LoadJsonContentParameters(TypedDict):
    file_path: PossibleValue
    json_path: PossibleNoneValue
    encoding: PossibleNoneValue


class LoadJsonContent(TypedDict):
    type: Literal["load_json_content"]
    parameters: _LoadJsonContentParameters
    property_name: NotRequired[str]


class _LoadYamlContentParameters(TypedDict):
    file_path: PossibleValue
    path_filter: PossibleNoneValue
    encoding: PossibleNoneValue


class LoadYamlContent(TypedDict):
    type: Literal["load_yaml_content"]
    parameters: _LoadYamlContentParameters
    property_name: NotRequired[str]


class _LoadTextContentParameters(TypedDict):
    file_path: PossibleValue
    encoding: PossibleNoneValue


class LoadTextContent(TypedDict):
    type: Literal["load_text_content"]
    parameters: _LoadTextContentParameters


####################
#
# functions - lambda
#
####################


class _FilterParameters(TypedDict):
    input_array: PossibleValue
    input_element: str
    expression: PossibleValue


class Filter(TypedDict):
    type: Literal["filter"]
    parameters: _FilterParameters


####################
#
# functions - logical
#
####################


class BoolFunc(TypedDict):
    type: Literal["bool"]
    parameters: _JsonParameters


####################
#
# functions - numeric
#
####################


class IntFunc(TypedDict):
    type: Literal["int"]
    parameters: _StringParameters


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
    property_name: NotRequired[str]


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


class _ListFuncParameters(TypedDict):
    func_name: PossibleValue
    resource_identifier: PossibleValue
    api_version: PossibleValue


class ListFunc(TypedDict):
    type: Literal["list_func"]
    parameters: _ListFuncParameters


class ManagementGroupResourceId(TypedDict):
    type: Literal["management_group_resource_id"]
    parameters: _TenantResourceIdParameters


class _PickZonesParameters(TypedDict):
    provider_namespace: PossibleValue
    resource_type: PossibleValue
    location: PossibleValue
    number_of_zones: PossibleNoneValue
    offset: PossibleNoneValue


class PickZones(TypedDict):
    type: Literal["pick_zones"]
    parameters: _PickZonesParameters


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


class _ManagementGroupParameters(TypedDict):
    identifier: PossibleNoneValue


class ManagementGroup(TypedDict):
    type: Literal["management_group"]
    parameters: _ManagementGroupParameters
    property_name: NotRequired[str]


class _ResourceGroupParameters(TypedDict):
    resource_group_name: PossibleNoneValue
    subscription_id: PossibleNoneValue


class ResourceGroup(TypedDict):
    type: Literal["resource_group"]
    parameters: _ResourceGroupParameters
    property_name: NotRequired[str]


class _SubscriptionParameters(TypedDict):
    subscription_id: PossibleNoneValue


class Subscription(TypedDict):
    type: Literal["subscription"]
    parameters: _SubscriptionParameters
    property_name: NotRequired[str]


class Tenant(TypedDict):
    type: Literal["tenant"]
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


class _DataUriParameters(TypedDict):
    string_to_convert: PossibleValue


class DataUri(TypedDict):
    type: Literal["data_uri"]
    parameters: _DataUriParameters


class _DataUriToStringParameters(TypedDict):
    data_uri_to_convert: PossibleValue


class DataUriToString(TypedDict):
    type: Literal["data_uri_to_string"]
    parameters: _DataUriToStringParameters


class EndsWith(TypedDict):
    type: Literal["ends_with"]
    parameters: _StartsWithParameters


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


class NewGuid(TypedDict):
    type: Literal["new_guid"]


class _PadLeftParameters(TypedDict):
    value_to_pad: PossibleValue
    total_length: PossibleValue
    padding_character: PossibleNoneValue


class PadLeft(TypedDict):
    type: Literal["pad_left"]
    parameters: _PadLeftParameters


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
    index: NotRequired[int]


class _JoinParameters(TypedDict):
    input_array: PossibleValue
    delimiter: PossibleValue


class Join(TypedDict):
    type: Literal["join"]
    parameters: _JoinParameters


class _StartsWithParameters(TypedDict):
    string_to_search: PossibleValue
    string_to_find: PossibleValue


class StartsWith(TypedDict):
    type: Literal["starts_with"]
    parameters: _StartsWithParameters


class _StringParameters(TypedDict):
    value_to_convert: PossibleValue


class String(TypedDict):
    type: Literal["string"]
    parameters: _StringParameters


class _SubstringParameters(TypedDict):
    string_to_parse: PossibleValue
    start_index: PossibleValue
    length: PossibleNoneValue


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


class _TrimParameters(TypedDict):
    string_to_trim: PossibleValue


class Trim(TypedDict):
    type: Literal["trim"]
    parameters: _TrimParameters


class UniqueString(TypedDict):
    type: Literal["unique_string"]
    parameters: _GuidParameters


class _UriParameters(TypedDict):
    base_uri: PossibleValue
    relative_uri: PossibleValue


class Uri(TypedDict):
    type: Literal["uri"]
    parameters: _UriParameters


class _UriComponentParameters(TypedDict):
    string_to_encode: PossibleValue


class UriComponent(TypedDict):
    type: Literal["uri_component"]
    parameters: _UriComponentParameters


class _UriComponentToStringParameters(TypedDict):
    uri_encoded_string: PossibleValue


class UriComponentToString(TypedDict):
    type: Literal["uri_component_to_string"]
    parameters: _UriComponentToStringParameters


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


class Divide(TypedDict):
    type: Literal["divide"]
    operands: _SubstractOperands


class _MinusOperands(TypedDict):
    integer_value: PossibleValue


class Minus(TypedDict):
    type: Literal["minus"]
    operands: _MinusOperands


class Modulo(TypedDict):
    type: Literal["modulo"]
    operands: _SubstractOperands


class Multiply(TypedDict):
    type: Literal["multiply"]
    operands: _SubstractOperands


class _SubstractOperands(TypedDict):
    operand_1: PossibleValue
    operand_2: PossibleValue


class Substract(TypedDict):
    type: Literal["substract"]
    operands: _SubstractOperands


####################
#
# Operators - accessor
#
####################


class _IndexAccessorOperands(TypedDict):
    operand_1: PossibleValue
    operand_2: PossibleValue


class IndexAccessor(TypedDict):
    type: Literal["index_accessor"]
    operands: _IndexAccessorOperands


class _FunctionAccessorOperands(TypedDict):
    operand_1: PossibleValue
    func_name: PossibleValue
    operand_2: NotRequired[PossibleValue]  # and many more possible


class FunctionAccessor(TypedDict):
    type: Literal["function_accessor"]
    operands: _FunctionAccessorOperands


class _NestedResourceAccessorOperands(TypedDict):
    operand_1: PossibleValue
    operand_2: PossibleValue


class NestedResourceAccessor(TypedDict):
    type: Literal["nested_resource_accessor"]
    operands: _NestedResourceAccessorOperands


class _PropertyAccessorOperands(TypedDict):
    operand_1: PossibleValue
    operand_2: PossibleValue


class PropertyAccessor(TypedDict):
    type: Literal["property_accessor"]
    operands: _PropertyAccessorOperands


####################
#
# JSON response
#
####################


class BicepJson(TypedDict):
    globals: GlobalsAttributes
    parameters: NotRequired[dict[str, ParameterAttributes]]
    variables: NotRequired[dict[str, VariableAttributes]]
    resources: NotRequired[dict[str, ResourceAttributes]]
    modules: NotRequired[dict[str, ModuleAttributes]]
    outputs: NotRequired[dict[str, OutputAttributes]]
