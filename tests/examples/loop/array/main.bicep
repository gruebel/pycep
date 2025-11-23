// variable
var stringArray = [for i in range(0, itemCount): 'item${(i + 1)}']

// output
output out1 array = [for i in bicepVarArray: {
  element: i
}]

// resource
resource storageArray 'Microsoft.Storage/storageAccounts@2021-06-01' = [for name in storageNames: {
  name: '${name}${uniqueString(resourceGroup().id)}'
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'Storage'
}]

// module
module sqlFirewallRules 'sql-firewall-rule.bicep' = [for firewallRules in sqlLogicalServer.firewallRules: {
  name: 'sqlFirewallRule-${uniqueString(sqlLogicalServer.name)}'
  params: {
    sqlFirewallRule: firewallRules
    sqlServerName: sqlLogicalServer.name
  }
}]

// property
resource parentResources 'Microsoft.Example/examples@2020-06-06' = [for parent in parents: {
  name: parent.name
  properties: {
    children: [for child in parent.children: {
      name: child.name
      setting: child.settingValue
    }]
  }
}]
