// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-files#loadtextcontent

// param
param paramStr string = loadTextContent('rules.json', 'utf-8')

// var
var cpuCores = loadTextContent(filePath, encoding)

// resource
resource identityProvider 'Microsoft.ApiManagement/service/identityProviders@2020-06-01-preview' = {
  name: 'exmple'
  properties: loadTextContent(filePath)
  dependsOn: [
    apiManagementService
  ]
}

// output
output ftpUser string = loadTextContent(filePath)

// namespace
output namespace string = sys.loadTextContent(filePath)
