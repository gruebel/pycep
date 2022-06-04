// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-date#datetimetoepoch

// param
param paramStr string = dateTimeToEpoch('4/7/2023 2:53:14 PM')

// var
var cpuCores = dateTimeToEpoch(epochValue)

// resource
resource identityProvider 'Microsoft.ApiManagement/service/identityProviders@2020-06-01-preview' = {
  name: dateTimeToEpoch(epochValue)
  properties: {
    clientId: 'googleClientId'
    clientSecret: googleClientSecret
  }
  dependsOn: [
    apiManagementService
  ]
}

// output
output ftpUser string = dateTimeToEpoch(epoch.value)

// namespace sys
output namespace string = sys.dateTimeToEpoch(epochValue)
