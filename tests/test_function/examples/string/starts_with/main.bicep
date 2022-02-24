// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-string#startswith

// param
param paramStr bool = startsWith('abcdef', 'ab')

// var
var varstr = startsWith(firstArray, intValue)

// resource
resource identityProvider 'Microsoft.ApiManagement/service/identityProviders@2020-06-01-preview' = {
  name: 'exmple'
  properties: startsWith(firstObject.names, name)
  dependsOn: [
    apiManagementService
  ]
}

// output
output ftpUser bool = startsWith(firstObject, 'some')

// namespace
output namespace bool = sys.startsWith(firstArray, '1')
