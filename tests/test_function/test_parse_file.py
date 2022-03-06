import json
from pathlib import Path

from assertpy import assert_that

from pycep import BicepParser

EXAMPLES_DIR = Path(__file__).parent / "examples/file"
BICEP_PARSER = BicepParser()


def test_parse_load_file_as_base64() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "load_file_as_base64"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BICEP_PARSER.parse(file_path=file_path)

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_load_text_content() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "load_text_content"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BICEP_PARSER.parse(file_path=file_path)

    # then
    assert_that(result).is_equal_to(expected_result)
