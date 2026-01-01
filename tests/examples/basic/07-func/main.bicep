// https://docs.azure.cn/en-us/azure-resource-manager/bicep/user-defined-functions

// definition
func buildUrl(https bool, hostname string, path string) string => '${https ? 'https' : 'http'}://${hostname}${empty(path) ? '' : '/${path}'}'

func sayHelloString(name string) string => 'Hi ${name}!'

func sayHelloObject(name string) object => {
  hello: 'Hi ${name}!'
}

func nameArray(name string) array => [
  name
]

func addNameArray(name string) array => [
  'Mary'
  'Bob'
  name
]

// usage
output azureUrl string = buildUrl(true, 'microsoft.com', 'azure')
output greetingArray array = map(['Evie', 'Casper'], name => sayHelloString(name))
output greetingObject object = sayHelloObject('John')
output nameArray array = nameArray('John')
output addNameArray array = addNameArray('John')
