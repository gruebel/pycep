// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-array#concat

// param
param paramStr array = concat(firstArray, secondArray)

// var
var cpuCores = concat(firstArray, secondArray)

// resource
resource identityProvider 'Microsoft.ApiManagement/service/identityProviders@2020-06-01-preview' = {
  name: 'exmple'
  properties: concat(firstArray)
  dependsOn: [
    apiManagementService
  ]
}

// output
output ftpUser object = concat(firstArray, secondArray, thirdArray)

// namespace sys
output namespace array = sys.concat(firstArray, secondArray)
