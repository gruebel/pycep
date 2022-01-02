// basic types
output stringOutput int = 42
output booleanOutput bool = false

// interpolation
output storageName string = '${toLower(storageNamePrefix)}${uniqueString(resourceGroup().id)}'

// expression
output location string = resourceGroup().location

// multi-line (no interpolation support yet)
output multilineOutput string = '''
this is multi-line
  string with formatting
  preserved.
'''
