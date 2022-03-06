// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-files#loadfileasbase64

// param
param paramStr string = loadFileAsBase64('rules.json')

// var
var cpuCores = loadFileAsBase64(filePath)

// resource
resource identityProvider 'Microsoft.ApiManagement/service/identityProviders@2020-06-01-preview' = {
  name: 'exmple'
  properties: loadFileAsBase64(filePath)
  dependsOn: [
    apiManagementService
  ]
}

// output
output ftpUser string = loadFileAsBase64(filePath)

// namespace
output namespace string = sys.loadFileAsBase64(filePath)
