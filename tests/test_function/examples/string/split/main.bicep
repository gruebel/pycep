// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-string#split

// param
param paramStr array = split('one,two,three', ',')

// var
var varStr = split(administratorAccountUsername, '@')

// resource
resource assignment 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: split(roleName, '.')
  properties: {
    roleDefinitionId: definition.id
    principalId: principalId
  }
}

// output
output ftpUser array = split(site.properties, '/')

// namespace sys
output namespace array = sys.split(site.properties, '/')
