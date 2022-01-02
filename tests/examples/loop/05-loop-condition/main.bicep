// resource
resource storageConidtion 'Microsoft.Storage/storageAccounts@2021-06-01' = [for i in range(0, storageCount): if(createNewStorage) {
  name: '${i}deploy${baseName}'
  params: {
    storageName: '${i}${baseName}'
    location: location
  }
}]
