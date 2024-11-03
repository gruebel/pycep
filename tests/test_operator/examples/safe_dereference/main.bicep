// https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/operator-safe-dereference

// resource
resource storage 'Microsoft.Storage/storageAccounts@2023-04-01' = [for i in range(0, storageCount): {
  name: storageAccountSettings[?i].?name ?? 'defaultname'
  location: storageAccountSettings[?i].?location ?? location
  kind: storageAccountSettings[?i].?kind ?? 'StorageV2'
  sku: {
    name: storageAccountSettings[?i].?sku ?? 'Standard_GRS'
  }
}]
