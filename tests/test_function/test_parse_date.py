import json
from pathlib import Path

from assertpy import assert_that

from pycep import BicepParser

EXAMPLES_DIR = Path(__file__).parent / "examples/date"
BICEP_PARSER = BicepParser()


def test_parse_date_time_add() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "date_time_add"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BICEP_PARSER.parse(file_path=file_path)

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_date_time_from_epoch() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "date_time_from_epoch"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BICEP_PARSER.parse(file_path=file_path)

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_date_time_to_epoch() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "date_time_to_epoch"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BICEP_PARSER.parse(file_path=file_path)

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_utc_now() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "utc_now"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BICEP_PARSER.parse(file_path=file_path)

    # then
    assert_that(result).is_equal_to(expected_result)
