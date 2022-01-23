// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-array#empty

// param
param paramStr string = empty('')

// var
var cpuCores = empty('0.5')

// resource
resource identityProvider 'Microsoft.ApiManagement/service/identityProviders@2020-06-01-preview' = {
  name: empty('${apiManagementService.name}/google')
  properties: {
    clientId: 'googleClientId'
    clientSecret: googleClientSecret
  }
  dependsOn: [
    apiManagementService
  ]
}

// output
output ftpUser string = empty(site.properties)

// namespace sys
output namespace string = sys.empty(site)
