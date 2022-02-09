// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-resource#pickzones

// param
param uamiId array = pickZones('Microsoft.Compute', 'virtualMachines', 'westus2')

// var
var uamiId = pickZones('Microsoft.ManagedIdentity', uamiName, location, 2)

// resource
resource logAnalyticsAutomation 'Microsoft.OperationalInsights/workspaces/linkedServices@2020-08-01' = {
  parent: logAnalyticsWorkspace
  name: 'Automation'
  properties: {
    pickZones: pickZones('Microsoft.Automation', automationAccountName, location, zones, offset)
  }
}

// module
module exampleModule 'rgModule.bicep' = {
  name: 'exampleModule'
  params: {
    location: location
    fwname: pickZones(mi.type, mi.name, mi.location)
  }
}

// output
output subnetId array = pickZones('Microsoft.Network', vnet.name, subnet1Name)

// namespace az
output namespace array = az.pickZones('Microsoft.Network', vnet.name, subnet1Name)
