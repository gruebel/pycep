// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-date#datetimefromepoch

// param
param paramStr string = dateTimeFromEpoch(1683040573)

// var
var cpuCores = dateTimeFromEpoch(epochValue)

// resource
resource identityProvider 'Microsoft.ApiManagement/service/identityProviders@2020-06-01-preview' = {
  name: dateTimeFromEpoch(epochValue)
  properties: {
    clientId: 'googleClientId'
    clientSecret: googleClientSecret
  }
  dependsOn: [
    apiManagementService
  ]
}

// output
output ftpUser string = dateTimeFromEpoch(epoch.value)

// namespace sys
output namespace string = sys.dateTimeFromEpoch(epochValue)
