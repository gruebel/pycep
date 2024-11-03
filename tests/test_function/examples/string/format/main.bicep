// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-string#format

// param
param paramStr array = format('{0}, {1}. Formatted number: {2:N0}', greeting, name, numberToFormat)

// var
var cpuCores = format(
  '-{0}-',
  greeting
)

// resource
resource identityProvider 'Microsoft.ApiManagement/service/identityProviders@2020-06-01-preview' = {
  name: 'exmple'
  properties: format('{0}, {1}', greeting, name)
  dependsOn: [
    format
  ]
}

// output
output ftpUser object = format('{0}, {1}', greeting, name)

// namespace sys
output namespace array = sys.format('{0}, {1}', greeting, name)
