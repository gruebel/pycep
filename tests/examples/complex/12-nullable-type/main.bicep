// https://docs.azure.cn/en-us/azure-resource-manager/bicep/data-types#nullable-types

// param
param name string?
param age int?

// var
var nullVar = null
var stringVar string? = null

// output
output description string? = name
output config object? = null
