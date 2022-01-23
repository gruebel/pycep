// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/operators-comparison#less-than-or-equal-

// parameter
param paramCompare bool = 6 <= 5

// variable
var varCompare = 'demo' <= 'damo'

// output
output outputCompare bool = firstString <= secondString

// resource
resource pip 'Microsoft.Network/publicIPAddresses@2020-06-01' = {
  name: publicIp.name
  location: publicIp.location
  properties: {
    ddosSettings: {
      protectedIP: publicIpLabel <= 'public'
    }
    publicIPAllocationMethod: 'Static'
  }
}
