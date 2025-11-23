@description('Name of the storage account')
var saName = 'example'

@description('Id of the resource group')
var rgId = resourceGroup().id

@export()
var myConstant = 'This is a constant value'
