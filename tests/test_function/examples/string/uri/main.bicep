// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-string#uri

// param
param paramStr string = uri('http://contoso.com/resources/', 'nested/azuredeploy.json')

// var
var varStr = uri(administratorAccountUsername, 'nested/azuredeploy.json')

// resource
resource assignment 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: uri(roleName, searchStr)
  properties: {
    roleDefinitionId: definition.id
    principalId: uri
  }
}

// output
output ftpUser string = uri(site.properties, 'nested/azuredeploy.json')

// namespace sys
output namespace string = sys.uri(site.properties, 'nested/azuredeploy.json')
