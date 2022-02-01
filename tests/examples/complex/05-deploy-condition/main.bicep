// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/conditional-resource-deployment#deploy-condition

resource sa 'Microsoft.Storage/storageAccounts@2019-06-01' = if (newOrExisting == 'new') {
  name: storageAccountName
  location: location
  sku: {
    name: 'Standard_LRS'
    tier: 'Standard'
  }
  kind: 'StorageV2'
  properties: {
    accessTier: 'Hot'
  }
}

module apimUsers './users.bicep' = if (deployUsers) {
  params: {
    apimInstanceName: apiManagement.name
  }
  name: 'apimUsers'
}
