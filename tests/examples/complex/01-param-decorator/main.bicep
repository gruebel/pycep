// allowed
@allowed([
  1
  2, 3
])
param zone int

@allowed([
  'one'
  'two'
])
param demoEnum string

// description
@description('Must be at least Standard_A3 to support 2 NICs.')
param virtualMachineSize string = 'Standard_DS1_v2'

// min/max length
@minLength(3)
param storageAccountName string

@maxLength(5)
param appNames array

// min/max value
@minValue(-1)
param month int

@maxValue(730)
param retentionInDays int

// metadata
@metadata({
  name: 'Module name'
  version: 'Module version or specify latest to get the latest version'
  uri: 'Module package uri, e.g. https://www.powershellgallery.com/api/v2/package'
})
param modules array = []

// secure
@secure()
param demoPassword string

// multiple decorators
@description('Password for the Virtual Machine.')
@minLength(12)
@secure()
param adminPassword string
