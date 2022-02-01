// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-date#datetimeadd

// param
param paramStr string = dateTimeAdd('2020-04-07 14:53:14Z', 'P3Y')

// var
var cpuCores = dateTimeAdd(baseTime, duration)

// resource
resource identityProvider 'Microsoft.ApiManagement/service/identityProviders@2020-06-01-preview' = {
  name: dateTimeAdd(baseTime, duration, formatStr)
  properties: {
    clientId: 'googleClientId'
    clientSecret: googleClientSecret
  }
  dependsOn: [
    apiManagementService
  ]
}

// output
output ftpUser string = dateTimeAdd(site.properties, 'PT1H')

// namespace sys
output namespace string = sys.dateTimeAdd(site.properties, 'PT1H')
