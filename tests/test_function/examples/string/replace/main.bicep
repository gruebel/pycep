// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-string#replace

// param
param roleAssignmentName string = replace(principalId, '/', '')

// var
var varStr = replace('something', 'e', 'f')

// resource
resource assignment 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: replace(roleName, principalId, otherId)
  properties: {
    roleDefinitionId: definition.id
    principalId: principalId
  }
}

// output
output ftpUser string = replace(site.properties, '{0}', 'osdisk')

// namespace sys
output namespace string = sys.replace(site.properties, '{0}', 'osdisk')
