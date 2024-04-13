// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-array#union

// param
param paramStr array = union(firstArray, secondArray)

// var
var cpuCores = union(firstArray, secondArray)

// resource
resource identityProvider 'Microsoft.ApiManagement/service/identityProviders@2020-06-01-preview' = {
  name: 'exmple'
  properties: union(firstObject, secondObject).tags
  dependsOn: [
    apiManagementService
  ]
}

resource applicationGateway 'Microsoft.Network/applicationGateways@2023-04-01' = {
  name: name
  properties: union({
      urlPathMaps: urlPathMaps
    }, (enableFips ? {
      enableFips: enableFips
    } : {}),
    (!empty(wafc) ? { webApplicationFirewallConfiguration: wafc } : {})
  )
  zones: zones
}

// output
output ftpUser object = union(firstObject, secondObject, thirdObject)

// namespace sys
output namespace array = sys.union(firstArray, secondArray)
