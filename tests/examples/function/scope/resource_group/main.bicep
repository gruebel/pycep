// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-scope#resourcegroup

// basic declaration
param paramObject object = resourceGroup()

var resourceGroupName = resourceGroup().name

// resource
resource managedidentity 'Microsoft.ManagedIdentity/userAssignedIdentities@2018-11-30' = {
  name: uamiName
  location: resourceGroup().location
}

// module (scope setting)
module exampleModule 'rgModule.bicep' = {
  name: 'exampleModule'
  scope: resourceGroup(resourceGroupName)
}

module exampleModuleSub 'rgModule.bicep' = {
  name: 'exampleModule'
  scope: resourceGroup(subscriptionId, resourceGroupName)
}

// output
output resourceGroupOutput object = resourceGroup()

// namespace az
output namespace object = az.resourceGroup()
