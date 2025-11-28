# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

# Added

- Support any kind of function via a fallback mechanism
- Support any kind of decorator via a fallback mechanism
- Support `range` function
- Support multiple NOT `!` operators in a single expression
- Support `@export` decorator
- Support `@sealed` decorator

# Changed

- Simplified function parsing, which reduced the startup time by multiple seconds
- Simplified decorator parsing, which reduced the overall parsing time by ~10%
- loop type `range` is now either of type `array` or `array_index` and the `array_name` stores the `range` function
- Improved support of lambda expressions
- Improved `property_accessor` and `index_accessor` parsing

## [0.6.1] - 2025-11-23

# Added

- Support Python 3.14 officially
- Support `extension` element
- Support typed variables
- Support nullable types
- Support `import` element
- Support loop and conditional blocks in child resources

# Changed

- Migrated the project to `uv`

# Removed

- Drop support of Python 3.8

## [0.5.1] - 2024-11-03

# Added

- Support Python 3.13 officially
- Support `loadYamlContent` function
- Support `flatten` function
- Initial support of custom data types
- Support safe-dereference operator

# Changed

- Fixed multiline issue with union function
- Fixed multiple newline issues

# Removed

- Drop support of Python 3.7

## [0.4.2] - 2023-11-05

# Added

- Support Python 3.12 officially
- Support all accessor operators
- Support `join` function
- Support `metadata` element
- Support more resource for `list*` function

### Changed

- Fixed a regression to support quoted keys with dots in an object
- Fixed typo in `join` parameter name

## [0.4.1] - 2023-06-18

# Added

- Support more list* accessor operators
- Support newlines between function parameters

### Changed

- Fixed an issue with function `resourceId` not allowing more than 5 parameters
- Fixed an issue with a final newline in the `@metadata` decorator

## [0.4.0] - 2023-04-29

### Added

- Support dot notation in private module registry names
- Support `sys` namespace notation for decorators
- Support `!` non-null operator
- Support `filter` function
- Support multi line strings in description decorator

### Changed

- Fixed an issue with comments between decorator and element

## [0.3.9] - 2022-08-30

### Changed

- Fixed an issue with unclosed multi line strings

## [0.3.8] - 2022-08-01

### Added

- Support `loadJsonContent` function

### Changed

- Support shadowing of a couple of built-in functions
- Support single line array and object declarations

## [0.3.7] - 2022-06-04

### Added

- Support index accessor for `json` function
- Support `managementGroupResourceId` function
- Support `dateTimeFromEpoch` function
- Support `dateTimeToEpoch` function

## [0.3.6] - 2022-05-21

### Added

- Support property accessor for `json` function
- Support Python 3.11 officially

## [0.3.5] - 2022-05-15

### Added

- Support `@description` decorator for var elements
- Leverage `typing.NotRequired` from Python 3.11 to improve type hints

## [0.3.4] - 2022-04-10

### Added

- Support `@description` decorator for output elements
- Support public module registry references
- Support module alias references

## [0.3.3] - 2022-03-21

### Changed

- Adjust the name of child resources to add the parent name as prefix to prevent overlap
- Moved `depends_on` to the `config` block

## [0.3.2] - 2022-03-14

### Added

- Add contribution guidelines `CONTRIBUTING.md`
- Support `LoadTextContent` function
- Support `loadFileAsBase64` function

### Changed

- Support negative values in `@minValue` decorator

## [0.3.1] - 2022-03-05

### Changed

- Remove usuage of `typing_extensions.NotRequired`
- Refactor `BicepParser` class to leverage lazy loading of the compiled grammar

## [0.3.0] - 2022-03-03

### Added

- First release to be able to parse all the official examples of Bicep [201](https://github.com/Azure/bicep/tree/main/docs/examples/201) and [301](https://github.com/Azure/bicep/tree/main/docs/examples/301).
- Enable caching of compiled parser
- Ignore shell styled comments
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

## [0.2.0] - 2022-02-13

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

## [0.1.0] - 2022-02-06

### Added

- First release to be able to parse all the official examples of Bicep [101](https://github.com/Azure/bicep/tree/main/docs/examples/101).

[Unreleased]: https://github.com/gruebel/pycep/compare/0.6.1...HEAD
[0.6.1]: https://github.com/gruebel/pycep/compare/0.5.1...0.6.1
[0.5.1]: https://github.com/gruebel/pycep/compare/0.4.2...0.5.1
[0.4.2]: https://github.com/gruebel/pycep/compare/0.4.1...0.4.2
[0.4.1]: https://github.com/gruebel/pycep/compare/0.4.0...0.4.1
[0.4.0]: https://github.com/gruebel/pycep/compare/0.3.9...0.4.0
[0.3.9]: https://github.com/gruebel/pycep/compare/0.3.8...0.3.9
[0.3.8]: https://github.com/gruebel/pycep/compare/0.3.7...0.3.8
[0.3.7]: https://github.com/gruebel/pycep/compare/0.3.6...0.3.7
[0.3.6]: https://github.com/gruebel/pycep/compare/0.3.5...0.3.6
[0.3.5]: https://github.com/gruebel/pycep/compare/0.3.4...0.3.5
[0.3.4]: https://github.com/gruebel/pycep/compare/0.3.3...0.3.4
[0.3.3]: https://github.com/gruebel/pycep/compare/0.3.2...0.3.3
[0.3.2]: https://github.com/gruebel/pycep/compare/0.3.1...0.3.2
[0.3.1]: https://github.com/gruebel/pycep/compare/0.3.0...0.3.1
[0.3.0]: https://github.com/gruebel/pycep/compare/0.2.0...0.3.0
[0.2.0]: https://github.com/gruebel/pycep/compare/0.1.0...0.2.0
[0.1.0]: https://github.com/gruebel/pycep/compare/24fc2a5...0.1.0
