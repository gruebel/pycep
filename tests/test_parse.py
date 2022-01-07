import json
from pathlib import Path

from assertpy import assert_that

from pycep import BicepParser

EXAMPLES_DIR = Path(__file__).parent / "examples"


# will change this to a more complex example, when decorators are supported
def test_parse_with_line_numbers() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "loop/02-loop-array"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result-line-numbers.json").read_text())

    # when
    result = BicepParser(file_path, add_line_numbers=True).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_param() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "basic/01-param"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_var() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "basic/02-var"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_output() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "basic/03-output"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_resource() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "basic/04-resource"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_module() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "basic/05-module"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_loop_index() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "loop/01-loop-index"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_loop_array() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "loop/02-loop-array"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_loop_array_index() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "loop/03-loop-array-index"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)
