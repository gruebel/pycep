// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-string#string

// param
param roleAssignmentName string = string(principalId)

// var
var varStr = string('something')

// resource
resource assignment 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: string(123)
  properties: {
    roleDefinitionId: definition.id
    principalId: principalId
  }
}

// output
output ftpUser string = string(site.properties)

// namespace sys
output namespace string = sys.string(site.properties)
