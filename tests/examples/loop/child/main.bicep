resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: storageAccountName

  resource tableService 'tableServices' = {
    name: 'default'

    resource tableList 'tables' = [for tableName in storageTables: {
      name: tableName
    }]
  }

  resource queueService 'queueServices' = {
    name: 'default'

    resource queueList 'queues' = [for queueName in storageQueues: {
      name: queueName
    }]
  }
}
