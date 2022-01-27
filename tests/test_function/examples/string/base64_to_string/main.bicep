// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-string#base64tostring

// param
param roleAssignmentName string = base64ToString(principalId)

// var
var varStr = base64ToString('something')

// resource
resource assignment 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: base64ToString('123')
  properties: {
    roleDefinitionId: definition.id
    principalId: principalId
  }
}

// output
output ftpUser string = base64ToString(site.properties)

// namespace sys
output namespace string = sys.base64ToString(site.properties)
