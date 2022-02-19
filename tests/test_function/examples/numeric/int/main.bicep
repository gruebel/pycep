// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-numeric#int

// param
param paramStr int = int(1)

// var
var cpuCores = int('0.5')

// resource
resource identityProvider 'Microsoft.ApiManagement/service/identityProviders@2020-06-01-preview' = {
  name: int(value)
  properties: {
    clientId: 'googleClientId'
    clientSecret: googleClientSecret
  }
}

// output
output ftpUser int = int(site.properties)

// namespace
output namespace int = sys.int(site.properties)
