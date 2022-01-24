// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-array#contains

// param
param paramStr bool = contains(firstArray, stringValue)

// var
var varstr = contains(firstArray, intValue)

// resource
resource identityProvider 'Microsoft.ApiManagement/service/identityProviders@2020-06-01-preview' = {
  name: 'exmple'
  properties: contains(firstObject.names, name)
  dependsOn: [
    apiManagementService
  ]
}

// output
output ftpUser bool = contains(firstObject, 'some')

// namespace sys
output namespace bool = sys.contains(firstArray, 1)
