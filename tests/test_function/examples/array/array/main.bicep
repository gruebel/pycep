// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-array

// param
param paramStr array = array('')

// var
var cpuCores = array(5)

// resource
resource identityProvider 'Microsoft.ApiManagement/service/identityProviders@2020-06-01-preview' = {
  name: array('${apiManagementService.name}/google')
  properties: {
    clientId: 'googleClientId'
    clientSecret: googleClientSecret
  }
  dependsOn: [
    apiManagementService
  ]
}

// output
output ftpUser array = array(site.properties)

// namespace sys
output namespace array = sys.array(site)
