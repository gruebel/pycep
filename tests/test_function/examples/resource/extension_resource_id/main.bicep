// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-resource#extensionresourceid

// param
param uamiId string = extensionResourceId(resourceId, 'Microsoft.ManagedIdentity/userAssignedIdentities', uamiName)

// var
var uamiId = extensionResourceId(id, 'Microsoft.ManagedIdentity/userAssignedIdentities', uamiName)

// resource
resource logAnalyticsAutomation 'Microsoft.OperationalInsights/workspaces/linkedServices@2020-08-01' = {
  parent: logAnalyticsWorkspace
  name: 'Automation'
  properties: {
    extensionResourceId: extensionResourceId(id, 'Microsoft.Automation/automationAccounts', automationAccountName)
  }
}

// module
module exampleModule 'rgModule.bicep' = {
  name: 'exampleModule'
  params: {
    location: location
    fwname: extensionResourceId(mi.id, mi.type, mi.name)
    extensionResourceId: id
  }
}

// output
output subnetId string = extensionResourceId(rId, 'Microsoft.Network/virtualNetworks/subnets', vnet.name, subnet1Name)

// namespace az
output namespace object = az.extensionResourceId(rId, 'Microsoft.Automation/automationAccounts', automationAccountName)
