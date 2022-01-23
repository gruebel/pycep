// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-resource#tenantresourceid

// param
param uamiId string = tenantResourceId('Microsoft.ManagedIdentity/userAssignedIdentities', 'acdd72a7-3385-48ef-bd42-f606fba81ae7')

// var
var uamiId = tenantResourceId('Microsoft.ManagedIdentity/userAssignedIdentities', uami, name)

// resource
resource logAnalyticsAutomation 'Microsoft.OperationalInsights/workspaces/linkedServices@2020-08-01' = {
  parent: logAnalyticsWorkspace
  name: 'Automation'
  properties: {
    tenantResourceId: tenantResourceId('Microsoft.Automation/automationAccounts', automationAccountName)
  }
}

// module
module exampleModule 'rgModule.bicep' = {
  name: 'exampleModule'
  params: {
    location: location
    fwname: tenantResourceId(mi.type, mi.name)
    tenantResourceId: id
  }
}

// output
output subnetId string = tenantResourceId('Microsoft.Network/virtualNetworks/subnets', vnet.name, subnet1Name)

// namespace az
output namespace object = az.tenantResourceId('Microsoft.Automation/automationAccounts', automationAccountName)
