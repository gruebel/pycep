// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/child-resource-name-type

resource storage 'Microsoft.Storage/storageAccounts@2021-02-01' = {
  name: 'examplestorage'
  location: resourceGroup().location
  kind: 'StorageV2'
  sku: {
    name: 'Standard_LRS'
  }

  resource service 'fileServices' = {
    name: 'default'

    resource share 'shares' = {
      name: 'exampleshare'
    }
  }
}

resource ts 'Microsoft.Resources/templateSpecs@2019-06-01-preview' existing = {
  scope: resourceGroup(templateSpecSub, templateSpecRg)
  name: templateSpecName

  // reference to existing version
  resource tsVersion 'versions' existing = {
    name: templateSpecVersion
  }
}
