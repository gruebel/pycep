// basic types
var stringVar = 'example value'
var exampleBool = true
var exampleInt = 1

// arrays
var mixedArray = [
  resourceGroup().name
  1
  // some comment
  true
  'example string'
  'comma', 'separated', 'elements'
]
var oneLineMixedArray = [ resourceGroup().name, 1, true, 'example string' ]

// objects
var mixedObject = {
  name: resourceGroup().name
  integer: 1
  // some comment
  boolean: true
  example: 'string'
}
var oneLineMixedObject = { name: resourceGroup().name, integer: 1, boolean: true, example: 'string'}

// interpolation
var storageName = '${toLower(storageNamePrefix)}${uniqueString(resourceGroup().id)}'

// multi-line (no interpolation support yet)
var stringVar = '''
this is multi-line
  string with formatting
  preserved.
'''
