// https://docs.azure.cn/en-us/azure-resource-manager/bicep/variables#typed-variables

// basic types
var resourceName string = 'myResource'
var instanceCount int = 3
var isProduction bool = true

// arrays
var mixedArray array = [
  resourceGroup().name
  1
  // some comment
  true
  'example string'
  'comma', 'separated', 'elements'
]
var subnets array = ['subnet1', 'subnet2']

// objects
var mixedObject object = {
  name: resourceGroup().name
  integer: 1
  // some comment
  boolean: true
  example: 'string'
}
var tags object = { environment: 'dev' }

// schema not supported yet
// var config {
//   name: string
//   count: int
//   enabled: bool
// } = {
//   name: 'myApp'
//   count: 5
//   enabled: true
// }
