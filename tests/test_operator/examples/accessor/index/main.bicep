// https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/operators-access#index-accessor

var location = 'westeurope'
var regions = {
  uksouth: 'uks'
  westeurope: 'we'
}
var shortLocation = regions[location]
var zones = {
  zone1: regions
  zone2: {}
}

output myRegion string = regions['uksouth']
output myZone string = zones.zone1['westeurope']
output region string = shortLocation
