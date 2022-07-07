// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-files#loadjsoncontent

// param
param paramStr string = loadJsonContent('rules.json', 'firstRule')

// var
var cpuCores = loadJsonContent(filePath, jsonPath, encoding)

// resource
resource identityProvider 'Microsoft.ApiManagement/service/identityProviders@2020-06-01-preview' = {
  name: 'example'
  properties: loadJsonContent(filePath)
  dependsOn: [
    apiManagementService
  ]
}

// output
output ftpUser string = loadJsonContent(filePath)

output ftpUserId string = loadJsonContent(filePath).id

output lateIndexed string = loadJsonContent('./vars.json').subscriptions[env].id

output directIndexed string = loadJsonContent('./vars.json')[sub].dev[var_id]

// namespace
output namespace string = sys.loadJsonContent(filePath)

// output
