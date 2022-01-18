# pycep

[![codecov](https://codecov.io/gh/gruebel/pycep/branch/master/graph/badge.svg?token=49WHVYGE1D)](https://codecov.io/gh/gruebel/pycep)
[![PyPI](https://img.shields.io/pypi/v/pycep-parser)](https://pypi.org/project/pycep-parser/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pycep-parser)](https://github.com/gruebel/pycep)

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
- [x] Comparison
  - [x] Greater than or equals
  - [x] Greater than
  - [x] Less than or equals
  - [x] Less than
  - [x] Equals
  - [x] Not equals
  - [x] Equals case-insensitive
  - [x] Not equals case-insensitive
- [ ] Logical
  - [ ] And
  - [ ] Or
  - [ ] Not
  - [ ] Coalesce
  - [x] Conditional expression

### CI/CD
- [x] Add test coverage

## Considering
- Adding line numbers to other parts

## Out-of-scope
- Bicep to ARM converter and vice versa
