// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-config-modules

// public registry
module publicRegistryModule 'br/public:samples/hello-world:1.0.2' = {
  name: 'helloWorld'
  params: {
    name: 'John Dole'
  }
}

// private registry
module privateRegistryModule 'br/ContosoRegistry:storage:v1' = {
  name: 'storageDeploy'
  params: {
    storagePrefix: 'examplestg1'
  }
}

module privateDotRegistryModule 'br/registry:microsoft.resources:1.2.3' = {
  name: 'helloWorld'
  params: {
    name: 'John Dole'
  }
}

// template spec
module templateModule 'ts/CoreSpecs:storage:v1' = {
  name: 'storageDeploy'
  params: {
    storagePrefix: 'examplestg1'
  }
}
