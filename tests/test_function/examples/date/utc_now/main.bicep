// https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-date#utcnow

// param
param currentTime string = utcNow()

param utcShortValue string = utcNow('d')
