import json
from pathlib import Path

from assertpy import assert_that

from pycep import BicepParser

EXAMPLES_DIR = Path(__file__).parent / "examples/loop"
BICEP_PARSER = BicepParser()


def test_parse_loop_array() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "array"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BICEP_PARSER.parse(file_path=file_path)

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_loop_array_index() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "array-index"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BICEP_PARSER.parse(file_path=file_path)

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_loop_object() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "object"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BICEP_PARSER.parse(file_path=file_path)

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_loop_condition() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "condition"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BICEP_PARSER.parse(file_path=file_path)

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_loop_range() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "range"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BICEP_PARSER.parse(file_path=file_path)

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_array_w_newline() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "array-w-newline"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BICEP_PARSER.parse(file_path=file_path)

    # then
    assert_that(result).is_equal_to(expected_result)
