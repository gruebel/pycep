# Supported capabilities

## Functions

### Any

[Reference](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-any)

- [x] Any

### Array

[Reference](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-array)

- [x] array
- [x] concat
- [x] contains
- [x] empty
- [x] first
- [ ] flatten
- [x] indexOf
- [x] intersection
- [ ] items
- [x] last
- [x] lastIndexOf
- [x] length
- [x] max
- [x] min
- [ ] range
- [x] skip
- [x] take
- [x] union

### CIDR

[Reference](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-cidr)

- [ ] cidrHost
- [ ] cidrSubnet
- [ ] parseCidr

### Date

[Reference](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-date)

- [x] dateTimeAdd
- [x] dateTimeFromEpoch
- [x] dateTimeToEpoch
- [x] utcNow

### Deployment

[Reference](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-deployment)

- [x] deployment
- [x] environment

### File

[Reference](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-files)

- [x] loadFileAsBase64
- [x] loadJsonContent
- [x] loadYamlContent
- [x] loadTextContent

### Lambda

[Reference](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-lambda)

- [x] filter
- [ ] map
- [ ] reduce
- [ ] sort
- [ ] toObject

### Logical

[Reference](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-logical)

- [x] bool

### Numeric

[Reference](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-numeric)

- [x] int
- [x] max
- [x] min

### Object

[Reference](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-object)

- [x] contains
- [x] empty
- [x] intersection
- [x] json
- [x] length
- [x] union

### Parameters file

[Reference](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-parameters-file)

- [ ] readEnvironmentVariable (only used in `.bicepparam` files)

### Resource

[Reference](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-resource)

- [x] extensionResourceId
- [ ] getSecret (used as a resource accessor)
- [x] listKeys (deprecated)
- [x] managementGroupResourceId
- [x] pickZones
- [ ] providers (deprecated)
- [x] reference
- [x] resourceId
- [x] subscriptionResourceId
- [x] tenantResourceId

### Scope

[Reference](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-scope)

- [x] managementGroup
- [x] resourceGroup
- [x] subscription
- [x] tenant

### String

[Reference](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-string)

- [x] base64
- [x] base64ToJson
- [x] base64ToString
- [x] concat
- [x] contains
- [x] dataUri
- [x] dataUriToString
- [x] empty
- [x] endsWith
- [x] first
- [x] format
- [x] guid
- [x] indexOf
- [x] join
- [x] last
- [x] lastIndexOf
- [x] length
- [x] newGuid
- [x] padLeft
- [x] replace
- [x] skip
- [x] split
- [x] startsWith
- [x] string
- [x] substring
- [x] take
- [x] toLower
- [x] toUpper
- [x] trim
- [x] uniqueString
- [x] uri
- [x] uriComponent
- [x] uriComponentToString

## Operators

### Accessor

[Reference](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/operators-access)

- [x] Index
- [x] Function
- [x] Nested resource
- [x] Property

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
- [x] Not (partially, but need further improvements)
- [x] Coalesce
- [x] Conditional expression

### Numeric

[Reference](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/operators-numeric)

- [x] Multiply
- [x] Divide
- [x] Modulo
- [x] Add
- [x] Subtract
- [x] Minus
