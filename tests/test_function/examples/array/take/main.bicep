// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-array#take

// param
param paramStr string = take('something', 4)

// var
var varstr = take(firstArray, intValue)

// resource
resource identityProvider 'Microsoft.ApiManagement/service/identityProviders@2020-06-01-preview' = {
  name: 'exmple'
  properties: take(firstObject.names, name)
  dependsOn: [
    apiManagementService
  ]
}

// output
output ftpUser array = take(firstArray, 2)

// namespace sys
output namespace array = sys.take(firstArray, 1)
