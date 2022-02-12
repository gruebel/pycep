import json
from pathlib import Path

from assertpy import assert_that

from pycep import BicepParser

EXAMPLES_DIR = Path(__file__).parent / "examples/numeric"


def test_parse_add() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "add"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_divide() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "divide"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_minus() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "minus"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_modulo() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "modulo"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_multiply() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "multiply"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_substract() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "substract"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path=file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)
