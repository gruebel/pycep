// https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-array#flatten

// param
param paramStr string = flatten(['one', 'two'])

// var
var varStr = flatten(administratorAccountUsername)

// resource
resource assignment 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: flatten(roleName).name
  properties: {
    roleDefinitionId: definition.id
    principalId: principalId
  }
}

// output
output ftpUser string = flatten(site.properties)

// namespace sys
output namespace string = sys.flatten(site.properties)
