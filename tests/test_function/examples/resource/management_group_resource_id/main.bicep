// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-resource#managementgroupresourceid

// param
param uamiId string = managementGroupResourceId('Microsoft.ManagedIdentity/userAssignedIdentities', 'acdd72a7-3385-48ef-bd42-f606fba81ae7')

// var
var uamiId = managementGroupResourceId('Microsoft.ManagedIdentity/userAssignedIdentities', uami, name)

// resource
resource logAnalyticsAutomation 'Microsoft.OperationalInsights/workspaces/linkedServices@2020-08-01' = {
  parent: logAnalyticsWorkspace
  name: 'Automation'
  properties: {
    managementGroupResourceId: managementGroupResourceId('Microsoft.Automation/automationAccounts', automationAccountName)
  }
}

// module
module exampleModule 'rgModule.bicep' = {
  name: 'exampleModule'
  params: {
    location: location
    fwname: managementGroupResourceId(mi.type, mi.name)
    managementGroupResourceId: id
  }
}

// output
output subnetId string = managementGroupResourceId('Microsoft.Network/virtualNetworks/subnets', vnet.name, subnet1Name)

// namespace az
output namespace object = az.managementGroupResourceId('Microsoft.Automation/automationAccounts', automationAccountName)
