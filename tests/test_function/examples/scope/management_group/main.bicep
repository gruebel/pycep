// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-scope#managementgroup

// param
param paramObject object = managementGroup()

// var
var id = managementGroup().id

// resource
resource managedidentity 'Microsoft.ManagedIdentity/userAssignedIdentities@2018-11-30' = {
  name: uamiName
  id: managementGroup().id
}

// module (scope setting)
module exampleModule 'rgModule.bicep' = {
  name: 'exampleModule'
  scope: managementGroup('/providers/Microsoft.Management/managementGroups/examplemg1')
}

// output
output subscriptionOutput object = managementGroup()

// namespace az
output namespace object = az.managementGroup()
