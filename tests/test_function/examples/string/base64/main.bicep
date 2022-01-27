// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-string#base64

// param
param roleAssignmentName string = base64(principalId)

// var
var varStr = base64('something')

// resource
resource assignment 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: base64('123')
  properties: {
    roleDefinitionId: definition.id
    principalId: principalId
  }
}

// output
output ftpUser string = base64(site.properties)

// namespace sys
output namespace string = sys.base64(site.properties)
