// https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-lambda#filter

// var
var diagnosticsLogsSpecified = [for category in filter(diagnosticLogCategoriesToEnable, item => item != 'allLogs'): {
  category: category
  enabled: true
  retentionPolicy: {
    enabled: true
    days: diagnosticLogsRetentionInDays
  }
}]

// resource
resource identityProvider 'Microsoft.ApiManagement/service/identityProviders@2020-06-01-preview' = {
  name: filter(itemForLoop, i => i > 5)
  properties: {
    clientId: 'googleClientId'
    clientSecret: googleClientSecret
  }
  dependsOn: [
    apiManagementService
  ]
}

// output
output oldDogs array = filter(dogs, dog => dog.age >=5)

// namespace sys
output namespace array = sys.filter(dogs, dog => dog.age >=5)
