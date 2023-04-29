// https://github.com/Azure/bicep/pull/9585

// index
var maybeNull = mightIncludeNull[0]!.key

// function
resource backupVault 'Microsoft.DataProtection/backupVaults@2022-03-01' existing = {
  name: last(split(resourceId, '/'))!
}
