// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-resource#list

// param
param uamiId object = listKeys(refId, apiVersion)

// var
var uamiId = listKeys(refId, '2020-09-01')

// resource
resource logAnalyticsAutomation 'Microsoft.OperationalInsights/workspaces/linkedServices@2020-08-01' = {
  parent: logAnalyticsWorkspace
  name: 'Automation'
  properties: {
    listKeys: listKeys(refId, apiVersion)
  }
}

// module
module exampleModule 'rgModule.bicep' = {
  name: 'exampleModule'
  params: {
    location: location
    fwname: listKeys(refId, apiVersion)
    listKeys: id
  }
}

// output
output subnetId object = listKeys(refId, apiVersion).primaryEndpoints.blob

// namespace az
output namespace object = az.listKeys(refId, apiVersion)
