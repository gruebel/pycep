// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-scope#subscription

// param
param paramObject object = subscription()

// var
var subId = subscription().id

// resource
resource managedidentity 'Microsoft.ManagedIdentity/userAssignedIdentities@2018-11-30' = {
  name: subscription
  subId: subscription().subscriptionId
}

// module (scope setting)
module exampleModule 'rgModule.bicep' = {
  name: 'exampleModule'
  scope: subscription(subscriptionId)
}

// output
output subscriptionOutput object = subscription()

// namespace az
output namespace object = az.subscription()
