// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-string#base64tojson

// param
param roleAssignmentName object = base64ToJson(principalId)

// var
var varStr = base64ToJson('J3tcJ29uZVwnOiBcJ2FcJ30n')

// resource
resource assignment 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: base64ToJson('J3tcJ29uZVwnOiBcJ2FcJ30n')
  properties: {
    roleDefinitionId: definition.id
    principalId: principalId
  }
}

// output
output ftpUser object = base64ToJson(site.properties)

// namespace sys
output namespace object = sys.base64ToJson(site.properties)
