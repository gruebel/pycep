// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-string#endswith

// param
param paramStr bool = endsWith('abcdef', 'ab')

// var
var varstr = endsWith(firstArray, intValue)

// resource
resource identityProvider 'Microsoft.ApiManagement/service/identityProviders@2020-06-01-preview' = {
  name: 'exmple'
  properties: endsWith(firstObject.names, name)
  dependsOn: [
    apiManagementService
  ]
}

// output
output ftpUser bool = endsWith(firstObject, 'some')

// namespace
output namespace bool = sys.endsWith(firstArray, '1')
