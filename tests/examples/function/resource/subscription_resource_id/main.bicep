// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-resource#subscriptionresourceid

// param
param uamiId string = subscriptionResourceId('Microsoft.ManagedIdentity/userAssignedIdentities', 'acdd72a7-3385-48ef-bd42-f606fba81ae7')

// var
var uamiId = subscriptionResourceId('Microsoft.ManagedIdentity/userAssignedIdentities', uami, name)

// resource
resource logAnalyticsAutomation 'Microsoft.OperationalInsights/workspaces/linkedServices@2020-08-01' = {
  parent: logAnalyticsWorkspace
  name: 'Automation'
  properties: {
    subscriptionResourceId: subscriptionResourceId('Microsoft.Automation/automationAccounts', automationAccountName)
  }
}

// module
module exampleModule 'rgModule.bicep' = {
  name: 'exampleModule'
  params: {
    location: location
    fwname: subscriptionResourceId(mi.type, mi.name)
    subscriptionResourceId: id
  }
}

// output
output subnetId string = subscriptionResourceId(subId, 'Microsoft.Network/virtualNetworks/subnets', vnet.name, subnet1Name)

// namespace az
output namespace object = az.subscriptionResourceId('Microsoft.Automation/automationAccounts', automationAccountName)
