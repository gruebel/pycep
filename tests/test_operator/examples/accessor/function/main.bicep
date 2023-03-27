// https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/operators-access#function-accessor

var kvName = 'kvTest'
var subscriptionId = 'gsfgsdfgsd'
var kvResourceGroup = 'rgTest'
var sqlServerName = 'sqlServer'
var adminLogin = 'admin'

resource kv 'Microsoft.KeyVault/vaults@2019-09-01' existing = {
  name: kvName
  scope: resourceGroup(subscriptionId, kvResourceGroup )
}

module sql './sql.bicep' = {
  name: 'deploySQL'
  params: {
    sqlServerName: sqlServerName
    adminLogin: adminLogin
    adminPassword: kv.getSecret('vmAdminPassword')
  }
}
