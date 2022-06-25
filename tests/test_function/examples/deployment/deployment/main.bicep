// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-deployment#deployment

// param
param paramStr object = deployment()

// var
var cpuCores = deployment()

// resource
resource identityProvider 'Microsoft.ApiManagement/service/identityProviders@2020-06-01-preview' = {
  name: deployment().name
  properties: {
    clientId: 'googleClientId'
    clientSecret: deployment
  }
  dependsOn: [
    apiManagementService
  ]
}

// output
output ftpUser object = deployment()

// namespace sys
output namespace object = az.deployment()
