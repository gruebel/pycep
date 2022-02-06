// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-logical#bool

// param
param paramStr bool = bool(true)

// var
var cpuCores = bool('0.5')

// resource
resource identityProvider 'Microsoft.ApiManagement/service/identityProviders@2020-06-01-preview' = {
  name: bool('${apiManagementService.name}/google')
  properties: {
    clientId: 'googleClientId'
    clientSecret: googleClientSecret
  }
}

// output
output ftpUser bool = bool(site.properties)

// namespace sys
output namespace bool = sys.bool(site.properties)
