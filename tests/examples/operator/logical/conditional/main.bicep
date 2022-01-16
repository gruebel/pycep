// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/operators-logical#conditional-expression--

// var
var subnetId = createNewVnet ? subnet.id : resourceId(vnetResourceGroupName, 'Microsoft.Network/virtualNetworks/subnets', vnetName, subnetName)

// resource
resource managementGroup 'Microsoft.Management/managementGroups@2020-05-01' = {
  name: managementGroupId
  properties: {
    displayName: managementGroupDisplayName
    details: {
      parent: {
        id: (empty(parentManagementGroupId)) ? '/providers/Microsoft.Management/managementGroups/${parentManagementGroupId}' : null
      }
    }
  }
}

// output
output endpoint string = deployStorage ? myStorageAccount.properties.primaryEndpoints.blob : ''
