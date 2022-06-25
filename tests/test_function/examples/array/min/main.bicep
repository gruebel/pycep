// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-array#min

// param
param paramStr int = min(firstArray, secondArray)

// var
var cpuCores = min(1, 2, 3, 4)

// resource
resource identityProvider 'Microsoft.ApiManagement/service/identityProviders@2020-06-01-preview' = {
  name: 'exmple'
  properties: min(firstArray)
  dependsOn: [
    min
  ]
}

// output
output ftpUser int = min(firstArray, secondArray, thirdArray)

// namespace
output namespace int = sys.min(firstArray, secondArray)
