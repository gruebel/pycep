// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/operators-logical#and-

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

// multiple - Term 'FUNCTION' need to be separated first
//output multiple bool = !(!true)
