import json
from pathlib import Path

from assertpy import assert_that

from pycep import BicepParser

EXAMPLES_DIR = Path(__file__).parent / "examples/deployment"


def test_parse_deployment() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "deployment"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_environment() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "environment"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)
