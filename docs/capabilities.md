# Supported capabilities

## Functions

### Any

[Reference](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-any)

- [x] Any

### Array

[Reference](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-array)

- [ ] array
- [ ] concat
- [ ] contains
- [x] empty
- [ ] first
- [ ] intersection
- [ ] items
- [ ] last
- [ ] length
- [ ] max
- [ ] min
- [ ] range
- [ ] skip
- [ ] take
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

- [ ] ...
- [x] guid
- [ ] ...

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
- [ ] Subtract
- [ ] Minus
