// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-string#tolower

// param
param roleAssignmentName string = toLower(principalId)

// var
var varStr = toLower('something')

// resource
resource assignment 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: toLower('ONE two Three')
  properties: {
    roleDefinitionId: definition.id
    principalId: principalId
  }
}

// output
output ftpUser string = toLower(site.properties)

// namespace sys
output namespace string = sys.toLower(site.properties)
