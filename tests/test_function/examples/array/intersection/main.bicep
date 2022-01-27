// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-array#intersection

// param
param paramStr array = intersection(firstArray, secondArray)

// var
var cpuCores = intersection(firstArray, secondArray)

// resource
resource identityProvider 'Microsoft.ApiManagement/service/identityProviders@2020-06-01-preview' = {
  name: 'exmple'
  properties: intersection(firstObject, secondObject).tags
  dependsOn: [
    apiManagementService
  ]
}

// output
output ftpUser object = intersection(firstObject, secondObject, thirdObject)

// namespace sys
output namespace array = sys.intersection(firstArray, secondArray)
