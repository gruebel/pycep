// local ref
module localModule '../storageAccount.bicep' = {
  name: 'storageDeploy'
  params: {
    storagePrefix: 'examplestg1'
  }
}

// public registry ref
module publicRegistryModule 'br:mcr.microsoft.com/bicep/samples/hello-world:1.0.2' = {
  name: 'helloWorld'
  params: {
    name: 'John Dole'
  }
}

// private registry ref
module privateRegistryModule 'br:exampleregistry.azurecr.io/bicep/modules/storage:v1' = {
  name: 'storageDeploy'
  params: {
    storagePrefix: 'examplestg1'
  }
}

// template spec ref
module templateModule 'ts:11111111-1111-1111-1111-111111111111/templateSpecsRG/storageSpec:2.0' = {
  name: 'storageDeploy'
  params: {
    storagePrefix: 'examplestg1'
  }
}
