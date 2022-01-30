# Supported capabilities

## Functions

### Any

[Reference](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-any)

- [x] Any

### Array

[Reference](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-array)

- [ ] array
- [ ] concat
- [x] contains
- [x] empty
- [ ] first
- [x] intersection
- [ ] items
- [ ] last
- [x] length
- [ ] max
- [ ] min
- [ ] range
- [ ] skip
- [x] take
- [x] union

### Date

[Reference](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-date)

- [x] dateTimeAdd
- [x] utcNow

### Object

[Reference](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-object)

- [x] contains
- [x] empty
- [x] intersection
- [x] json
- [x] length
- [x] union

### Resource

[Reference](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-resource)

- [x] extensionResourceId
- [ ] getSecret
- [ ] list*
- [ ] pickZones
- [ ] providers (deprecated)
- [ ] reference
- [x] resourceId
- [x] subscriptionResourceId
- [x] tenantResourceId

### Scope

[Reference](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-scope)

- [ ] managementGroup
- [x] resourceGroup
- [x] subscription
- [ ] tenant

### String

[Reference](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-string)

- [x] base64
- [x] base64ToJson
- [x] base64ToString
- [ ] concat
- [x] contains
- [ ] dataUri
- [ ] dataUriToString
- [x] empty
- [ ] endsWith
- [ ] first
- [ ] format
- [x] guid
- [x] indexOf
- [ ] last
- [x] lastIndexOf
- [x] length
- [ ] newGuid
- [ ] padLeft
- [x] replace
- [ ] skip
- [x] split
- [ ] startsWith
- [x] string
- [x] substring
- [x] take
- [x] toLower
- [x] toUpper
- [ ] trim
- [x] uniqueString
- [ ] uri
- [ ] uriComponent
- [ ] uriComponentToString

## Operators

### Accessor

[Reference](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/operators-access)

- [ ] Index
- [ ] Function
- [ ] Nested resource
- [ ] Property

### Comparison

[Reference](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/operators-comparison)

- [x] Greater than or equals
- [x] Greater than
- [x] Less than or equals
- [x] Less than
- [x] Equals
- [x] Not equals
- [x] Equals case-insensitive
- [x] Not equals case-insensitive

### Logical

[Reference](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/operators-logical)

- [x] And
- [x] Or
- [x] Not (partially, but need firther improvements)
- [x] Coalesce
- [x] Conditional expression

### Numeric

[Reference](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/operators-numeric)

- [ ] Multiply
- [ ] Divide
- [ ] Modulo
- [ ] Add
- [x] Subtract
- [ ] Minus
