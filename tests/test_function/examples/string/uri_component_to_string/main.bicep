// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-string#uricomponenttostring

// param
param paramStr string = uriComponentToString('http%3A%2F%2Fcontoso.com%2Fresources%2F')

// var
var varStr = uriComponentToString(administratorAccountUsername)

// resource
resource assignment 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: uriComponentToString(roleName)
  properties: {
    roleDefinitionId: definition.id
    principalId: principalId
  }
}

// output
output ftpUser string = uriComponentToString(site.properties)

// namespace sys
output namespace string = sys.uriComponentToString(site.properties)
