import json
from pathlib import Path

import pytest
from assertpy import assert_that

from pycep import BicepParser
from pycep.transformer import BicepElement

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


def test_parse_playground_and_check_bicep_elements() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "complete/playground"
    file_path = sub_dir_path / "main.bicep"

    # when
    result = BicepParser(text=file_path.read_text()).json()

    # then
    vm_config = result["resources"]["vm"]["config"]
    assert_that(vm_config["name"]).is_instance_of(BicepElement)
    assert_that(vm_config["location"]).is_instance_of(BicepElement)
    assert_that(vm_config["properties"]["osProfile"]["computerName"]).is_instance_of(BicepElement)
    assert_that(vm_config["properties"]["osProfile"]["adminUsername"]).is_instance_of(BicepElement)
    assert_that(vm_config["properties"]["osProfile"]["adminPassword"]).is_instance_of(BicepElement)
    assert_that(vm_config["properties"]["hardwareProfile"]["vmSize"]).is_instance_of(BicepElement)


def test_constructor_error_with_text_and_file_path_parameters() -> None:
    # given
    sub_dir_path = EXAMPLES_DIR / "complete/playground"
    file_path = sub_dir_path / "main.bicep"

    # when
    with pytest.raises(TypeError) as exc_info:
        BicepParser(file_path=file_path, text=file_path.read_text())

    # then
    assert_that(str(exc_info.value)).is_equal_to("Either 'text' or 'file_path' can be set")


def test_constructor_error_with_missing_parameters() -> None:
    # when
    with pytest.raises(TypeError) as exc_info:
        BicepParser()

    # then
    assert_that(str(exc_info.value)).is_equal_to("Either 'text' or 'file_path' has to be set")
