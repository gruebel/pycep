// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-string#substring

// param
param roleAssignmentName string = substring(principalId, 1, 5)

// var
var varStr = substring('something', 1)

// resource
resource assignment 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: substring(roleName, principalId)
  properties: {
    roleDefinitionId: definition.id
    principalId: principalId
  }
}

// output
output ftpUser string = substring(site.properties, 3)

// namespace sys
output namespace string = sys.substring(site.properties, 3)
