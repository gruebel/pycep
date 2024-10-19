// variable
var resourceAccessRules = [
  for (id, item) in networkAccess_resource: {
    tenantId: az.subscription().tenantId
    resourceId: networkAccess_resource[item]
  }
]

// output
output deployedNSGs array = [
    for (name, i) in orgNames: {
      orgName: name
      nsgName: nsg[i].name
      resourceId: nsg[i].id
    }
]

// resource
/*
resource storageAccount_resource 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: storageAccountName
  location: location
  tags: tags
  sku: {
    name: storageAccountType
  }
  kind: storageAccountKind
  properties: {
    accessTier: storageAccountAccessTier
    minimumTlsVersion: 'TLS1_2'
    supportsHttpsTrafficOnly: true
    allowBlobPublicAccess: false
    allowCrossTenantReplication: true
    encryption: {
      keySource: 'Microsoft.Storage'
      requireInfrastructureEncryption: false
      services: {
        blob: {
          enabled: true
          keyType: 'Account'
        }
        file: {
          enabled: true
          keyType: 'Account'
        }
        queue: {
          enabled: true
          keyType: 'Account'
        }
        table: {
          enabled: true
          keyType: 'Account'
        }
      }
    }
    isHnsEnabled: storageAccountHnsEnabled
    isLocalUserEnabled: false
    isNfsV3Enabled: false
    isSftpEnabled: false
    keyPolicy: {
      keyExpirationPeriodInDays: 90
    }
    largeFileSharesState: 'Disabled'
    publicNetworkAccess: 'Enabled'
    networkAcls: {
      resourceAccessRules: networkAccess_resource == [''] || networkAccess_resource == [] ? [] : resourceAccessRules
      bypass: 'AzureServices'
      defaultAction: networkAccess_default
      virtualNetworkRules: empty(networkingResourceGroupName) && empty(virtualNetworkName) && empty(virtualNetworkSubnetName)
        ? []
        : [
            {
              id: virtualNetwork_resource::subnet.id
              action: 'Allow'
            }
          ]
    }
  }
}
*/

// module
module sqlLogicalServer 'sql-logical-server.bicep' = [
    for (sqlLogicalServer, index) in sqlLogicalServers: {
      name: 'sqlLogicalServer-${index}'
      params: {
        sqlLogicalServer: union(defaultSqlLogicalServerProperties, sqlLogicalServer)
        password: sqlLogicalServer.passwordFromKeyVault.secretName
        tags: union(tags, union(defaultSqlLogicalServerProperties, sqlLogicalServer).tags)
      }
    }
]
