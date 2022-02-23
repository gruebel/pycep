// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-scope#tenant

// param
param paramObject object = tenant()

// var
var id = tenant().id

// resource
resource managedidentity 'Microsoft.ManagedIdentity/userAssignedIdentities@2018-11-30' = {
  name: uamiName
  id: tenant().id
}

// module (scope setting)
module exampleModule 'rgModule.bicep' = {
  name: 'exampleModule'
  scope: tenant()
}

// output
output subscriptionOutput object = tenant()

// namespace az
output namespace object = az.tenant()
