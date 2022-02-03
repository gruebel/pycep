// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/operators-numeric#minus--

// param
param paramExpr int = - 2

// var
var varExpr = -4

// resource
resource managementGroup 'Microsoft.Management/managementGroups@2020-05-01' = {
  name: managementGroupId
  properties: {
    displayName: managementGroupDisplayName
    details: {
      parent: {
        id: -varExpr
      }
    }
  }
}

// output
output outputExpr int = -(5)

// more than two
output multiple bool = -(-5)
