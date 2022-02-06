// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-array#last

// param
param paramStr string = last('one,two,three')

// var
var varStr = last(administratorAccountUsername)

// resource
resource assignment 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: last(roleName).name
  properties: {
    roleDefinitionId: definition.id
    principalId: principalId
  }
}

// output
output ftpUser string = last(site.properties)

// namespace sys
output namespace string = sys.last(site.properties)
