// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/operators-logical#coalesce-

// param
param paramExpr bool = null ?? false

// var
var varExpr = null ?? null

// resource
resource managementGroup 'Microsoft.Management/managementGroups@2020-05-01' = {
  name: managementGroupId
  properties: {
    displayName: managementGroupDisplayName
    details: {
      parent: {
        id: varExpr ?? true
      }
    }
  }
}

// output
output outputExpr bool = paramExpr && varExpr

// more than two
output multiple bool = null && paramExpr && null && varExpr
