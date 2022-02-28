// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-string#datauri

// param
param roleAssignmentName string = dataUri(principalId)

// var
var varStr = dataUri('something')

// resource
resource assignment 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: dataUri('ONE two Three')
  properties: {
    roleDefinitionId: definition.id
    principalId: principalId
  }
}

// output
output ftpUser string = dataUri(site.properties)

// namespace
output namespace string = sys.dataUri(site.properties)
