// https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/operators-access#index-accessor

var location = 'westeurope'
var regions = {
  uksouth: 'uks'
  westeurope: 'we'
}
var shortLocation = regions[location]

output myRegion string = regions[location]
output region string = shortLocation
