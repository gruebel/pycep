// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-string#uricomponent

// param
param paramStr string = uriComponent('http://contoso.com/resources/')

// var
var varStr = uriComponent(administratorAccountUsername)

// resource
resource assignment 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: uriComponent(roleName)
  properties: {
    roleDefinitionId: definition.id
    principalId: principalId
  }
}

// output
output ftpUser string = uriComponent(site.properties)

// namespace sys
output namespace string = sys.uriComponent(site.properties)
