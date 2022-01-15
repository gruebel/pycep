import json
from pathlib import Path

from assertpy import assert_that

from pycep import BicepParser

EXAMPLES_DIR = Path(__file__).parent / "examples/operator"


def test_parse_conditional() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "conditional"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_equals() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "equals"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_not_equals() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "not_equals"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)
