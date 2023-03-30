import json
from pathlib import Path

from assertpy import assert_that

from pycep import BicepParser

EXAMPLES_DIR = Path(__file__).parent / "examples"
BICEP_PARSER = BicepParser()


def test_parse_index_accessor() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "accessor/index"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BICEP_PARSER.parse(file_path=file_path)
    # print(result)
    # print(BICEP_PARSER.create_tree(file_path=file_path))

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_function_accessor() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "accessor/function"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BICEP_PARSER.parse(file_path=file_path)

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_nested_resource_accessor() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "accessor/nested_resource"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BICEP_PARSER.parse(file_path=file_path)

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_property_accessor() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "accessor/property"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BICEP_PARSER.parse(file_path=file_path)

    # then
    assert_that(result).is_equal_to(expected_result)
