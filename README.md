# pycep

[![codecov](https://codecov.io/gh/gruebel/pycep/branch/master/graph/badge.svg?token=49WHVYGE1D)](https://codecov.io/gh/gruebel/pycep)
[![PyPI](https://img.shields.io/pypi/v/pycep-parser)](https://pypi.org/project/pycep-parser/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pycep-parser)](https://github.com/gruebel/pycep)
![CodeQL](https://github.com/gruebel/pycep/workflows/CodeQL/badge.svg)

A fun little project, which has the goal to parse
[Azure Bicep](https://github.com/Azure/bicep) files.
This is still a very early stage, therefore a lot can and will change.

## Current capabalities

[Supported capabilities](docs/capabilities.md)

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

### Functions
- [x] Any
- [ ] Array
  - [ ] array
  - [ ] concat
  - [ ] contains
  - [x] empty
  - [ ] first
  - [ ] intersection
  - [ ] items
  - [ ] last
  - [ ] length
  - [ ] max
  - [ ] min
  - [ ] range
  - [ ] skip
  - [ ] take
  - [x] union
- Resource
  - [x] extensionResourceId
  - [ ] getSecret
  - [ ] list*
  - [ ] pickZones
  - [ ] reference
  - [x] resourceId
  - [x] subscriptionResourceId
  - [x] tenantResourceId
- [ ] Scope
  - [ ] managementGroup
  - [x] resourceGroup
  - [x] subscription
  - [ ] tenant

### Operators
- [ ] Accessor
- [ ] Numeric

### CI/CD
- [ ] Fix security issues found by Scorecard

## Considering
- Adding line numbers to other parts

## Out-of-scope
- Bicep to ARM converter and vice versa
