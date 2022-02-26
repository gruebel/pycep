// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-string#trim

// param
param roleAssignmentName string = trim(principalId)

// var
var varStr = trim('something')

// resource
resource assignment 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: trim('ONE two Three')
  properties: {
    roleDefinitionId: definition.id
    principalId: principalId
  }
}

// output
output ftpUser string = trim(site.properties)

// namespace
output namespace string = sys.trim(site.properties)
