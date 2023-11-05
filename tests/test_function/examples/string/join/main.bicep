// https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-string#join

// param
param paramStr string = join(firstArray, delimiter)

// var
var cpuCores = join(firstArray, ',')

// resource
resource identityProvider 'Microsoft.ApiManagement/service/identityProviders@2020-06-01-preview' = {
  name: 'exmple'
  properties: join(firstArray, ';')
  dependsOn: [
    apiManagementService
  ]
}

// output
output ftpUser string = join(firstArray, ',')

// namespace sys
output namespace string = sys.join(firstArray, ',')
