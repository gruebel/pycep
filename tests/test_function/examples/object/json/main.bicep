// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-object#json

// param
param paramStr string = json('null')

// var
var varStr = json('{\'a\': \'b\'}')

// resource
resource identityProvider 'Microsoft.ApiManagement/service/identityProviders@2020-06-01-preview' = {
  name: json(someJsonObject)
  properties: {
    clientId: 'googleClientId'
    clientSecret: googleClientSecret
  }
  dependsOn: [
    apiManagementService
  ]
}

// output
output ftpUser string = json(site.properties)

// namespace sys
output namespace string = sys.json(site)
