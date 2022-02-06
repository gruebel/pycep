// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-array#first

// param
param paramStr string = first('one,two,three')

// var
var varStr = first(administratorAccountUsername)

// resource
resource assignment 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: first(roleName).name
  properties: {
    roleDefinitionId: definition.id
    principalId: principalId
  }
}

// output
output ftpUser string = first(site.properties)

// namespace sys
output namespace string = sys.first(site.properties)
