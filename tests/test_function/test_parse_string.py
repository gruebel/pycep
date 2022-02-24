import json
from pathlib import Path

from assertpy import assert_that

from pycep import BicepParser

EXAMPLES_DIR = Path(__file__).parent / "examples/string"


def test_parse_base64() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "base64"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_base64_to_json() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "base64_to_json"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_base64_to_string() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "base64_to_string"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_format() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "format"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_guid() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "guid"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_index_of() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "index_of"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_last_index_of() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "last_index_of"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_new_guid() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "new_guid"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_replace() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "replace"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_split() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "split"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_starts_with() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "starts_with"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_string() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "string"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_substring() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "substring"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_to_lower() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "to_lower"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_to_upper() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "to_upper"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_unique_string() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "unique_string"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_uri() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "uri"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_uri_component() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "uri_component"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_uri_component_to_string() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "uri_component_to_string"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)
