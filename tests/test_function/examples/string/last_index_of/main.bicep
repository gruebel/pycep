// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-string#lastindexof

// param
param paramStr int = lastIndexOf('one,two,three', ',')

// var
var varStr = lastIndexOf(administratorAccountUsername, '@')

// resource
resource assignment 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: lastIndexOf(roleName, searchStr)
  properties: {
    roleDefinitionId: definition.id
    principalId: principalId
  }
}

// output
output ftpUser int = lastIndexOf(site.properties, '/')

// namespace sys
output namespace int = sys.lastIndexOf(site.properties, '/')
