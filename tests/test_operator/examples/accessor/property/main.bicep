// https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/operators-access#property-accessor

var x = {
  y: {
    z: 'Hello'
    a: true
  }
  q: 42
}

output outputZ string = x.y.z
output outputQ int = x.q
