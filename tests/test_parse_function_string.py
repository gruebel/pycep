import json
from pathlib import Path

from assertpy import assert_that

from pycep import BicepParser

EXAMPLES_DIR = Path(__file__).parent / "examples/function/string"


def test_parse_guid() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "guid"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)
