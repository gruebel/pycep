// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/operators-comparison#not-equal-

// int
param intEqual bool = 5 != 6

// bool
var firstBool = true != false

// string
var elementEqual = 'demo' != 'demo'

// array
var arrayEqual = [
  1
  2
  3
] != [
  1
  2
  3
]

var objectEqual = {
  prop2: 'val2'
  prop1: 'val1'
} != {
  prop1: 'valX'
  prop2: 'valY'
}

// elements
output elementEqual bool = firstString != secondString
