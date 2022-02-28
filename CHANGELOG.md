# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

### Added

- Support `max` function
- Support `min` function
- Support `int` function
- Support `skip` function
- Support `managementGroup` function
- Support `tenant` function
- Support `startsWith` function
- Support `endsWith` function
- Support `trim` function
- Support `padLeft` function
- Support `dataUri` function
- Support `dataUriToString` function

## 0.2.0 - 2022-02-13

### Added

- Possibility to pass Bicep template via `str` or `Path`
- Add `BicepElement` to `json` output to differentiate between strings and element references
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
- Prioritize `_RESOURCE_ID` and `_RESOURCE_GROUP` over `STRING` terminal

## 0.1.0 - 2022-02-06

### Added

- First release to be able to parse all the official examples of Bicep [101](https://github.com/Azure/bicep/tree/main/docs/examples/101).
