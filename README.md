# pycep

[![Build Status](https://github.com/gruebel/pycep/workflows/CI/badge.svg)](https://github.com/gruebel/pycep/actions)
[![codecov](https://codecov.io/gh/gruebel/pycep/branch/master/graph/badge.svg?token=49WHVYGE1D)](https://codecov.io/gh/gruebel/pycep)
[![PyPI](https://img.shields.io/pypi/v/pycep-parser)](https://pypi.org/project/pycep-parser/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pycep-parser)](https://github.com/gruebel/pycep)
![CodeQL](https://github.com/gruebel/pycep/workflows/CodeQL/badge.svg)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/gruebel/pycep/badge)](https://api.securityscorecards.dev/projects/github.com/gruebel/pycep)

A parser for [Azure Bicep](https://github.com/Azure/bicep) files leveraging [Lark](https://github.com/lark-parser/lark).

## Getting Started

### Requirements

- Python 3.7+
- Lark 1.1.2+

### Install

```shell
pip install --upgrade pycep-parser
```

## Current capabilities

[Supported capabilities](docs/capabilities.md)

## Next milestones

### Functions
- [x] Any
- [ ] Array (in progress)
- [x] Date
- [x] Deployment
- [x] File
- [x] Logical
- [x] Numeric
- [x] Object
- [x] Resource
- [x] Scope
- [x] String

### Operators
- [ ] Accessor
- [x] Numeric

### Considering
- 1st class support of interpolated strings

### Out-of-scope
- Bicep to ARM converter and vice versa

## Contributing

Further details can be found in the [contribution guidelines](CONTRIBUTING.md).
