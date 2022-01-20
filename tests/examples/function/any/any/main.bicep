// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-any#any

// param
param paramStr string = any(true)

// var
var cpuCores = any('0.5')

// resource
resource identityProvider 'Microsoft.ApiManagement/service/identityProviders@2020-06-01-preview' = {
  name: any('${apiManagementService.name}/google')
  properties: {
    clientId: 'googleClientId'
    clientSecret: googleClientSecret
  }
  dependsOn: [
    apiManagementService
  ]
}

// output
output ftpUser string = any(site.properties)

// namespace sys
output namspace string = sys.any(site.properties)
