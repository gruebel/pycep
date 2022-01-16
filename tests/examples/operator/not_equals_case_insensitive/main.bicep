// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/operators-comparison#not-equal-case-insensitive-

// parameter
param paramEqual bool = 'demo' !~ 'Demo'

// variable
var varEqual = 'demo' !~ 'Demo'

// output
output outputEqual bool = firstString !~ secondString

// resource
resource pip 'Microsoft.Network/publicIPAddresses@2020-06-01' = {
  name: publicIp.name
  location: publicIp.location
  properties: {
    ddosSettings: {
      protectedIP: publicIpLabel !~ 'internal'
    }
    publicIPAllocationMethod: 'Static'
  }
}
