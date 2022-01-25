// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-string#indexof

// param
param paramStr int = indexOf('one,two,three', ',')

// var
var varStr = indexOf(administratorAccountUsername, '@')

// resource
resource assignment 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: indexOf(roleName, searchStr)
  properties: {
    roleDefinitionId: definition.id
    principalId: principalId
  }
}

// output
output ftpUser int = indexOf(site.properties, '/')

// namespace sys
output namespace int = sys.indexOf(site.properties, '/')
