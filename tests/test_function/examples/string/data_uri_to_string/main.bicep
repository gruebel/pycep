// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-string#datauritostring

// param
param roleAssignmentName string = dataUriToString(principalId)

// var
var varStr = dataUriToString('data:;base64,SGVsbG8sIFdvcmxkIQ==')

// resource
resource assignment 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: dataUriToString('data:;base64,SGVsbG8sIFdvcmxkIQ==')
  properties: {
    roleDefinitionId: definition.id
    principalId: principalId
  }
}

// output
output ftpUser string = dataUriToString(site.properties)

// namespace
output namespace string = sys.dataUriToString(site.properties)
