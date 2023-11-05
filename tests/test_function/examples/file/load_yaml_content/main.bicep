// https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-files#loadyamlcontent

// param
param paramStr string = loadYamlContent('rules.yaml', 'firstRule')

// var
var cpuCores = loadYamlContent(filePath, yamlPath, encoding)

// resource
resource identityProvider 'Microsoft.ApiManagement/service/identityProviders@2020-06-01-preview' = {
  name: 'example'
  properties: loadYamlContent(filePath)
  dependsOn: [
    apiManagementService
  ]
}

// output
output ftpUser string = loadYamlContent(filePath)

output ftpUserId string = loadYamlContent(filePath).id

output lateIndexed string = loadYamlContent('./vars.yaml').subscriptions[env].id

output directIndexed string = loadYamlContent('./vars.yaml')[sub].dev[var_id]

// namespace
output namespace string = sys.loadYamlContent(filePath)

// output
