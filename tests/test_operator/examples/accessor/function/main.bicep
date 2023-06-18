// https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/operators-access#function-accessor

// resource
resource dScript 'Microsoft.Resources/deploymentScripts@2019-10-01-preview' = {
  name: 'scriptWithStorage'
  location: location
  properties: {
    azCliVersion: '2.0.80'
    storageAccountSettings: {
      storageAccountName: storageAccount.name
      storageAccountKey: storageAccount.listKeys().keys[0].value
    }
  }
}

// module
module sql './sql.bicep' = {
  name: 'deploySQL'
  params: {
    sqlServerName: sqlServerName
    adminLogin: adminLogin
    adminPassword: kv.getSecret('vmAdminPassword')
  }
}

// output
output subnetId string = storageAccount.listAccountSas('2021-04-01', accountSasProperties).accountSasToken
