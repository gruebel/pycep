// https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/user-defined-data-types

// symbolic reference
type myStringType = string
type myOtherStringType = myStringType

// primitive literals
type myStringLiteralType = 'bicep' | 'arm' | 'azure'
type myIntLiteralType = 10
type myBoolLiteralType = true

// arrays not supported yet
//type myStrStringsType1 = string[]
//type myStrStringsType2 = ('a' | 'b' | 'c')[]
//type myIntArrayOfArraysType = int[][]
//type myMixedTypeArrayType = ('fizz' | 42 | {an: 'object'} | null)[]

// objects
type storageAccountConfigType = {
  name: string
  sku: string?
}

// decorators inside object not supported yet
// union type inside object not supported yet

type invalidRecursiveObjectType = {
  level1: {
    level2: {
      level3: {
        level4: {
          level5: invalidRecursiveObjectType
        }
      }
    }
  }
}

// unary operators
type negativeIntLiteral = -10
type negatedIntReference = -negativeIntLiteral

type negatedBoolLiteral = !true
type negatedBoolReference = !negatedBoolLiteral

// union types
type oneOfSeveralObjects = {foo: 'bar'} | {fizz: 'buzz'} | {snap: 'crackle'}
