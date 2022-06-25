// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-deployment#environment

// param
param paramStr object = environment()

// var
var cpuCores = environment()

// resource
resource identityProvider 'Microsoft.ApiManagement/service/identityProviders@2020-06-01-preview' = {
  name: environment().name
  properties: {
    clientId: 'googleClientId'
    clientSecret: environment
  }
  dependsOn: [
    apiManagementService
  ]
}

// output
output ftpUser object = environment()

// namespace sys
output namespace object = az.environment()
