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
    clientSecret: json
  }
  dependsOn: [
    apiManagementService
  ]
}

// output
output ftpUser string = json(site.properties).id

output lateIndexed string = json(loadTextContent('./vars.json')).subscriptions[env].id

output directIndexed string = json(loadTextContent('./vars.json'))[sub].dev[var_id]

// namespace sys
output namespace string = sys.json(site)
