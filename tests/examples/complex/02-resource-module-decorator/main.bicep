// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/loops#deploy-in-batches

// resource
@batchSize(2)
resource storageAcct 'Microsoft.Storage/storageAccounts@2021-06-01' = [for i in range(0, 4): {
  name: '${i}storage${uniqueString(resourceGroup().id)}'
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'Storage'
}]

// module
@batchSize(1)
module sqlLogicalServer 'sql-logical-server.bicep' = [for (sqlLogicalServer, index) in sqlLogicalServers: {
  name: 'sqlLogicalServer-${index}'
  params: {
    sqlLogicalServer: union(defaultSqlLogicalServerProperties, sqlLogicalServer)
    password: sqlPassKeyVaults[index].getSecret(sqlLogicalServer.passwordFromKeyVault.secretName)
    tags: union(tags, union(defaultSqlLogicalServerProperties, sqlLogicalServer).tags)
  }
}]
