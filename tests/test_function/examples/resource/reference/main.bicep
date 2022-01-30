// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-resource#reference

// param
param uamiId object = reference(refId, apiVersion)

// var
var uamiId = reference(refId, '2020-09-01', 'full')

// resource
resource logAnalyticsAutomation 'Microsoft.OperationalInsights/workspaces/linkedServices@2020-08-01' = {
  parent: logAnalyticsWorkspace
  name: 'Automation'
  properties: {
    reference: reference(refId, apiVersion)
  }
}

// module
module exampleModule 'rgModule.bicep' = {
  name: 'exampleModule'
  params: {
    location: location
    fwname: reference(refId, apiVersion)
    reference: id
  }
}

// output
output subnetId object = reference(refId).primaryEndpoints.blob

// namespace az
output namespace object = az.reference(refId)
