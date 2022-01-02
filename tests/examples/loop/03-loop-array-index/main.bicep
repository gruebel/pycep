// resource
resource storageArrayIndex 'Microsoft.Storage/storageAccounts@2021-06-01' = [for (config, i) in storageConfigurations: {
  name: '${storageAccountNamePrefix}${config.suffix}${i}'
  location: resourceGroup().location
  sku: {
    name: config.sku
  }
  kind: 'StorageV2'
}]
