// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/operators-numeric#add-

// param
param paramExpr int = 1 + 2

// var
var varExpr = 2+3

// resource
resource managementGroup 'Microsoft.Management/managementGroups@2020-05-01' = {
  name: managementGroupId
  properties: {
    displayName: managementGroupDisplayName
    details: {
      parent: {
        id: varExpr + 5
      }
    }
  }
}

// output
output outputExpr int = paramExpr + varExpr

// more than two
output multiple int = (paramExpr + varExpr + 5)
