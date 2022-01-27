// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-string#toupper

// param
param roleAssignmentName string = toUpper(principalId)

// var
var varStr = toUpper('something')

// resource
resource assignment 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: toUpper('ONE two Three')
  properties: {
    roleDefinitionId: definition.id
    principalId: principalId
  }
}

// output
output ftpUser string = toUpper(site.properties)

// namespace sys
output namespace string = sys.toUpper(site.properties)
