// https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/operators-logical#not-

// param
param paramExpr bool = !true

// var
var varExpr = !false

// resource
resource managementGroup 'Microsoft.Management/managementGroups@2020-05-01' = {
  name: managementGroupId
  properties: {
    displayName: managementGroupDisplayName
    details: {
      parent: {
        id: !varExpr
      }
    }
  }
}

// output
output outputExpr bool = !(paramExpr)
output multiple bool = !(!true)
