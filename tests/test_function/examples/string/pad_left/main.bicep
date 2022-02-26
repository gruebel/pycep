// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-string#padleft

// param
param roleAssignmentName string = padLeft(principalId, 1, 'x')

// var
var varStr = padLeft('something', 1)

// resource
resource assignment 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: padLeft(roleName, principalId)
  properties: {
    roleDefinitionId: definition.id
    principalId: principalId
  }
}

// output
output ftpUser string = padLeft(site.properties, 3)

// namespace
output namespace string = sys.padLeft(site.properties, 3)
