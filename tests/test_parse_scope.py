import json
from pathlib import Path

from assertpy import assert_that

from pycep import BicepParser

EXAMPLES_SCOPE_DIR = Path(__file__).parent / "examples/scope"


def test_parse_scope_resource_group() -> None:
    sub_dir_path = EXAMPLES_SCOPE_DIR / "01-scope-resource-group"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_scope_subscription() -> None:
    sub_dir_path = EXAMPLES_SCOPE_DIR / "02-scope-subscription"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_scope_management_group() -> None:
    sub_dir_path = EXAMPLES_SCOPE_DIR / "03-scope-management-group"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)


def test_parse_scope_tenant() -> None:
    sub_dir_path = EXAMPLES_SCOPE_DIR / "04-scope-tenant"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)
