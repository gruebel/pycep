# pycep

![PyPI](https://img.shields.io/pypi/v/pycep-parser)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pycep-parser)

A fun little project, which has the goal to parse
[Azure Bicep](https://github.com/Azure/bicep) files.
This is still a very early stage, therefore a lot can and will change.

## Next milestones

### General
- [x] Complete loop support
- [x] Param decorator
- [x] Resource/Module decorator
- [x] Target scope
- [ ] Existing resource keyword
- [ ] Module alias
- [ ] Deployment condition
- [x] Adding line numbers to element blocks

### Operators
- [ ] Comparison
  - [ ] Greater than or equal
  - [ ] Greater than
  - [ ] Less than or equal
  - [ ] Less than
  - [x] Equals
  - [x] Not equals
  - [ ] Equals case-insensitive
  - [ ] Not equals case-insensitive
- [ ] Logical
  - [ ] And
  - [ ] Or
  - [ ] Not
  - [ ] Coalesce
  - [x] Conditional expression

### CI/CD
- [x] Create a package
- [x] Publish package to `pypi`
- [ ] Add GitHub workflow for PR & master branch

## Considering
- Adding line numbers to other parts

## Out-of-scope
- Bicep to ARM converter and vice versa
