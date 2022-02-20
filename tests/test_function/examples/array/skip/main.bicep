// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-array#skip

// param
param paramStr array = skip(firstArray, number)

// var
var varstr = skip('some text', 3)

// resource
resource identityProvider 'Microsoft.ApiManagement/service/identityProviders@2020-06-01-preview' = {
  name: 'exmple'
  properties: skip(firstObject.names, name)
  dependsOn: [
    apiManagementService
  ]
}

// output
output ftpUser string = skip(value, 2)

// namespace sys
output namespace string = sys.skip(value, 2)
