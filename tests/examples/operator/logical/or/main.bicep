// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/operators-logical#or-

// param
param paramExpr bool = true || false

// var
var varExpr = true || false

// resource
resource managementGroup 'Microsoft.Management/managementGroups@2020-05-01' = {
  name: managementGroupId
  properties: {
    displayName: managementGroupDisplayName
    details: {
      parent: {
        id: varExpr || true
      }
    }
  }
}

// output
output outputExpr bool = paramExpr || varExpr

// more than two
output multiple bool = true || paramExpr || false || varExpr
