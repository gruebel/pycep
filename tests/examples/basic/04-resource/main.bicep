// basic
resource storageAccount 'Microsoft.Storage/storageAccounts@2019-06-01' = {
  name: '${toLower(storageNamePrefix)}${uniqueString(resourceGroup().id)}'
  location: resourceGroup().location
  sku: {
    name: storageAccountType
  }
  kind: 'StorageV2'
  properties: {
    networkAcls: {
      bypass: 'string'
      defaultAction: 'string'
      ipRules: [
        {
          action: 'Allow'
          value: 'string'
        }
      ]
      resourceAccessRules: [
        {
          resourceId: 'string'
          tenantId: 'string'
        }
      ]
      virtualNetworkRules: [
        {
          action: 'Allow'
          id: 'string'
          state: 'string'
        }
      ]
    }
  }
}
