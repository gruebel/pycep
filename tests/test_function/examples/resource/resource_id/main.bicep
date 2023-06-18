// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-resource#resourceid

// param
param uamiId string = resourceId('Microsoft.ManagedIdentity/userAssignedIdentities', uamiName)

// var
var uamiId = resourceId(subId, rgName, 'Microsoft.ManagedIdentity/userAssignedIdentities', uamiName)

// resource
resource logAnalyticsAutomation 'Microsoft.OperationalInsights/workspaces/linkedServices@2020-08-01' = {
  parent: logAnalyticsWorkspace
  name: 'Automation'
  properties: {
    resourceId: resourceId('Microsoft.Automation/automationAccounts', automationAccountName)
  }
}

// module
module exampleModule 'rgModule.bicep' = {
  name: 'exampleModule'
  params: {
    location: location
    fwname: resourceId(mi.type, mi.name)
  }
}

// output
output subnetId string = resourceId(subId, rgName, 'Microsoft.Network/virtualNetworks/subnets', vnet.name, subnet1Name, rangeName, ipName)

// namespace az
output namespace object = az.resourceId('Microsoft.Automation/automationAccounts', automationAccountName)
