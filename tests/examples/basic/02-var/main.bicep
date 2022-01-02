// basic types
var stringVar = 'example value'
var exampleBool = true
var exampleInt = 1

// array
var mixedArray = [
  resourceGroup().name
  1
  true
  'example string'
]

// interpolation
var storageName = '${toLower(storageNamePrefix)}${uniqueString(resourceGroup().id)}'

// multi-line (no interpolation support yet)
var stringVar = '''
this is multi-line
  string with formatting
  preserved.
'''
