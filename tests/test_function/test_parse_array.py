import json
from pathlib import Path

from assertpy import assert_that

from pycep import BicepParser

EXAMPLES_DIR = Path(__file__).parent / "examples/array"


def test_parse_array() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "array"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_concat() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "concat"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_contains() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "contains"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_empty() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "empty"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_first() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "first"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_intersection() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "intersection"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_last() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "last"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_length() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "length"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_take() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "take"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_union() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "union"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)
