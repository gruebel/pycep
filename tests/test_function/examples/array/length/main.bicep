// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-array#length

// param
param paramStr int = length('one,two,three')

// var
var varStr = length(administratorAccountUsername)

// resource
resource assignment 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: length(roleName)
  properties: {
    roleDefinitionId: definition.id
    principalId: length
  }
}

// output
output ftpUser int = length(site.properties)

// namespace sys
output namespace int = sys.length(site.properties)
