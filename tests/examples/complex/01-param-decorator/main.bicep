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

@sys.description('Required. The IDs of the principals to assign the role to.')
param principalIds array

@description('''
Optional. Resource ID of an already existing subnet, e.g.: /subscriptions/<subscriptionId>/resourceGroups/<resourceGroupName>/providers/Microsoft.Network/virtualNetworks/<vnetName>/subnets/<subnetName>.
If no value is provided, a new temporary VNET and subnet will be created in the staging resource group and will be deleted along with the remaining temporary resources.
''')
param subnetId string = ''

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

@metadata(
  {
    monthDays: 'Days of the month that the job should execute on. Must be between 1 and 31.'
    monthlyOccurrences: 'Occurrences of days within a month.'
    weekDays: 'Days of the week that the job should execute on.'
  }
)
param advancedSchedule object = {}

// secure
@secure()
param demoPassword string

// multiple decorators
@description('Password for the Virtual Machine.')
@minLength(12)
@secure()
#disable-next-line secure-secrets-in-params // Not a secret
param adminPassword string
