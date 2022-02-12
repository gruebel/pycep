# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

### Added

- Possibility to pass Bicep template via `str` or `Path`
- Support `first` function
- Support `last` function
- Support `bool` function
- Support `newGuid` function
- Support `uri` function
- Support `uriComponent` function
- Support `uriComponentToString` function
- Support `divide` operator
- Support `modulo` operator
- Support `multiply` operator
- Support `pickZones` function

### Changed

- Rename `loop_index` to `loop_range` and adjust the behaviour to allow iterating over item + index
- Prioritize `substract` over `minus` operator

## 0.1.0 - 2022-02-06

### Added

- First release to be able to parse all the official examples of Bicep [101](https://github.com/Azure/bicep/tree/main/docs/examples/101).
