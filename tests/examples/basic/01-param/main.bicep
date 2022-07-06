// basic declaration
param demoString string
param demoInt int

// default
param demoParam string = 'Contoso'
param demoBool bool = false

// array
param demoArray array = [
  resourceGroup().name
  1
  true
  'example string'
  'comma', 'separated', 'elements'
]

// object
param demoObject object = {
  name: resourceGroup().name
  number: 1
  boolean: true
  string: 'example string'
  single: 'line', comma: 'separated strings'
}

// expression
param location string = resourceGroup().location

// interpolation
param siteName string = 'site-${uniqueString(resourceGroup().id)}'

// multi-line (no interpolation support yet)
param multilineOutput string = '''
this is multi-line
  string with formatting
  preserved.
'''
