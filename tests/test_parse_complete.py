import json
from pathlib import Path

from assertpy import assert_that

from pycep import BicepParser

EXAMPLES_DIR = Path(__file__).parent / "examples"


def test_parse_playground_via_text() -> None:
    sub_dir_path = EXAMPLES_DIR / "complete/playground"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_playground_via_file_path() -> None:
    sub_dir_path = EXAMPLES_DIR / "complete/playground"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(text=file_path.read_text()).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_playground_with_line_numbers() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "complete/playground"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result-line-numbers.json").read_text())

    # when
    result = BicepParser(file_path=file_path, add_line_numbers=True).json()

    # then
    assert_that(result).is_equal_to(expected_result)
