// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-string#uniquestring

// param
param roleAssignmentName string = uniqueString(principalId, roleDefinitionId, rgName)

// var
var varStr = uniqueString('something', 'else')

// resource
resource assignment 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: uniqueString(roleName, principalId)
  properties: {
    roleDefinitionId: definition.id
    principalId: principalId
  }
}

// output
output ftpUser string = uniqueString(site.properties)

// namespace sys
output namespace string = sys.uniqueString(site.properties)
