@export()
type myObjectType = {
  foo: string
  bar: int
}

@sealed()
type anObject = {
  property: string
  optionalProperty: string?
}
