// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-array#max

// param
param paramStr int = max(firstArray, secondArray)

// var
var cpuCores = max(1, 2, 3, 4)

// resource
resource identityProvider 'Microsoft.ApiManagement/service/identityProviders@2020-06-01-preview' = {
  name: 'exmple'
  properties: max(firstArray)
  dependsOn: [
    apiManagementService
  ]
}

// output
output ftpUser int = max(firstArray, secondArray, thirdArray)

// namespace
output namespace int = sys.max(firstArray, secondArray)
