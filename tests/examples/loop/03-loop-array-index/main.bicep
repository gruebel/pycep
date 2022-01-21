// variable

// output
output deployedNSGs array = [for (name, i) in orgNames: {
  orgName: name
  nsgName: nsg[i].name
  resourceId: nsg[i].id
}]

// resource
resource storageArrayIndex 'Microsoft.Storage/storageAccounts@2021-06-01' = [for (config, i) in storageConfigurations: {
  name: '${storageAccountNamePrefix}${config.suffix}${i}'
  location: resourceGroup().location
  sku: {
    name: config.sku
  }
  kind: 'StorageV2'
}]

// module
module sqlLogicalServer 'sql-logical-server.bicep' = [for (sqlLogicalServer, index) in sqlLogicalServers: {
  name: 'sqlLogicalServer-${index}'
  params: {
    sqlLogicalServer: union(defaultSqlLogicalServerProperties, sqlLogicalServer)
    password: sqlLogicalServer.passwordFromKeyVault.secretName
    tags: union(tags, union(defaultSqlLogicalServerProperties, sqlLogicalServer).tags)
  }
}]
