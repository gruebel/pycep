// output
output inputObjKeys array = [for item in items(inputObj): item.key]

// resource
resource nsgObject 'Microsoft.Network/networkSecurityGroups@2020-06-01' = [for nsg in items(nsgValues): {
  name: nsg.value.name
  location: nsg.value.location
}]
