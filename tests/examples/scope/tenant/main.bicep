// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-to-tenant

targetScope = 'tenant'

param deploymentName string = 'managementGroups${utcNow()}'

module managementGroupGlobal './main.bicep' = {
  name: '${deploymentName}managementGroupGlobal'
  params: {
    managementGroupDisplayName: 'MyOrganisation'
    managementGroupId: 'gbl-org-mgp'
    subscriptionIds: []
  }
}

module managementGroupPlatform './main.bicep' = {
  name: '${deploymentName}managementGroupSandbox'
  params: {
    managementGroupDisplayName: 'Sandbox'
    managementGroupId: 'sbx-org-mgp'
    parentManagementGroupId: managementGroupGlobal.outputs.managementGroupID
    subscriptionIds: [
      '63c1651a-ec30-4f6c-a3ec-671e23063585'
    ]
  }
}
