// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-string#guid

// param
param roleAssignmentName string = guid(principalId, roleDefinitionId, rgName)

// var
var varStr = guid('something', 'else')

// resource
resource assignment 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: guid(roleName, principalId)
  properties: {
    roleDefinitionId: definition.id
    principalId: guid
  }
}

// output
output ftpUser string = guid(site.properties)

// namespace sys
output namespace string = sys.guid(site.properties)
