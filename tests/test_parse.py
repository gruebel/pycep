import json
from pathlib import Path

from assertpy import assert_that

from pycep import BicepParser

EXAMPLES_DIR = Path(__file__).parent / "examples"


def test_parse_param():
    # given
    file_path = EXAMPLES_DIR / "basic/01-param/main.bicep"

    # when
    result = BicepParser(file_path).json()

    # then
    assert_that(result).is_equal_to(
        {
            "parameters": {
                "demoString": {"type": "string", "default": None},
                "demoInt": {"type": "int", "default": None},
                "demoParam": {"type": "string", "default": "'Contoso'"},
                "demoBool": {"type": "bool", "default": False},
                "demoArray": {
                    "type": "array",
                    "default": ["resourceGroup().name", 1, True, "'example string'"],
                },
                "location": {"type": "string", "default": "resourceGroup().location"},
                "siteName": {
                    "type": "string",
                    "default": "'site-${uniqueString(resourceGroup().id)}'",
                },
                "multilineOutput": {
                    "type": "string",
                    "default": "'this is multi-line\n  string with formatting\n  preserved.\n'",
                },
            }
        }
    )


def test_parse_var():
    # given
    file_path = EXAMPLES_DIR / "basic/02-var/main.bicep"

    # when
    result = BicepParser(file_path).json()

    # then
    assert_that(result).is_equal_to(
        {
            "variables": {
                "stringVar": {"value": "'this is multi-line\n  string with formatting\n  preserved.\n'"},
                "exampleBool": {"value": True},
                "exampleInt": {"value": 1},
                "mixedArray": {"value": ["resourceGroup().name", 1, True, "'example string'"]},
                "storageName": {"value": "'${toLower(storageNamePrefix)}${uniqueString(resourceGroup().id)}'"},
            }
        }
    )


def test_parse_output():
    # given
    file_path = EXAMPLES_DIR / "basic/03-output/main.bicep"

    # when
    result = BicepParser(file_path).json()

    # then
    assert_that(result).is_equal_to(
        {
            "outputs": {
                "stringOutput": {"type": "int", "default": 42},
                "booleanOutput": {"type": "bool", "default": False},
                "storageName": {
                    "type": "string",
                    "default": "'${toLower(storageNamePrefix)}${uniqueString(resourceGroup().id)}'",
                },
                "location": {"type": "string", "default": "resourceGroup().location"},
                "multilineOutput": {
                    "type": "string",
                    "default": "'this is multi-line\n  string with formatting\n  preserved.\n'",
                },
            }
        }
    )


def test_parse_resource():
    # given
    file_path = EXAMPLES_DIR / "basic/04-resource/main.bicep"

    # when
    result = BicepParser(file_path).json()

    # then
    assert_that(result).is_equal_to(
        {
            "resources": {
                "storageAccount": {
                    "type": "Microsoft.Storage/storageAccounts",
                    "api_version": "2019-06-01",
                    "config": {
                        "name": "'${toLower(storageNamePrefix)}${uniqueString(resourceGroup().id)}'",
                        "location": "resourceGroup().location",
                        "sku": {"name": "storageAccountType"},
                        "kind": "'StorageV2'",
                        "properties": {
                            "networkAcls": {
                                "bypass": "'string'",
                                "defaultAction": "'string'",
                                "ipRules": [{"action": "'Allow'", "value": "'string'"}],
                                "resourceAccessRules": [{"resourceId": "'string'", "tenantId": "'string'"}],
                                "virtualNetworkRules": [{"action": "'Allow'", "id": "'string'", "state": "'string'"}],
                            }
                        },
                    },
                }
            }
        }
    )


def test_parse_module():
    # given
    file_path = EXAMPLES_DIR / "basic/05-module/main.bicep"

    # when
    result = BicepParser(file_path).json()

    # then
    assert_that(result).is_equal_to(
        {
            "modules": {
                "localModule": {
                    "type": "local",
                    "detail": {"full": "../storageAccount.bicep", "path": "../storageAccount.bicep"},
                    "config": {"name": "'storageDeploy'", "params": {"storagePrefix": "'examplestg1'"}},
                },
                "registryModule": {
                    "type": "bicep_registry",
                    "detail": {
                        "full": "exampleregistry.azurecr.io/bicep/modules/storage:v1",
                        "registry_name": "exampleregistry",
                        "path": "bicep/modules/storage",
                        "tag": "v1",
                    },
                    "config": {"name": "'storageDeploy'", "params": {"storagePrefix": "'examplestg1'"}},
                },
                "templateModule": {
                    "type": "template_spec",
                    "detail": {
                        "full": "11111111-1111-1111-1111-111111111111/templateSpecsRG/storageSpec:2.0",
                        "subscription_id": "11111111-1111-1111-1111-111111111111",
                        "resource_group_id": "templateSpecsRG",
                        "name": "storageSpec",
                        "version": "2.0",
                    },
                    "config": {"name": "'storageDeploy'", "params": {"storagePrefix": "'examplestg1'"}},
                },
            }
        }
    )


def test_parse_loop_index():
    # given
    file_path = EXAMPLES_DIR / "loop/01-loop-index/main.bicep"

    # when
    result = BicepParser(file_path).json()

    # then
    assert_that(result).is_equal_to(
        {
            "variables": {
                "stringArray": {
                    "value": {
                        "loop_type": {
                            "type": "index",
                            "detail": {
                                "index_name": "i",
                                "start_index": "0",
                                "count": "itemCount",
                            },
                        },
                        "condition": None,
                        "config": "'item${(i + 1)}'",
                    }
                }
            },
            "outputs": {
                "storageInfo": {
                    "type": "array",
                    "default": {
                        "loop_type": {
                            "type": "index",
                            "detail": {
                                "index_name": "i",
                                "start_index": "0",
                                "count": "storageCount",
                            },
                        },
                        "condition": None,
                        "config": {
                            "id": "storageAcct[i].id",
                            "blobEndpoint": "storageAcct[i].properties.primaryEndpoints.blob",
                            "status": "storageAcct[i].properties.statusOfPrimary",
                        },
                    },
                }
            },
            "resources": {
                "storageIndex": {
                    "type": "Microsoft.Storage/storageAccounts",
                    "api_version": "2021-06-01",
                    "config": {
                        "loop_type": {
                            "type": "index",
                            "detail": {
                                "index_name": "i",
                                "start_index": "0",
                                "count": "2",
                            },
                        },
                        "condition": None,
                        "config": {
                            "name": "'${i}storage${uniqueString(resourceGroup().id)}'",
                            "location": "location",
                            "sku": {
                                "name": "'Standard_LRS'",
                            },
                            "kind": "'Storage'",
                        },
                    },
                }
            },
            "modules": {
                "stgModule": {
                    "type": "local",
                    "detail": {
                        "full": "./storageAccount.bicep",
                        "path": "./storageAccount.bicep",
                    },
                    "config": {
                        "loop_type": {
                            "type": "index",
                            "detail": {
                                "index_name": "i",
                                "start_index": "0",
                                "count": "storageCount",
                            },
                        },
                        "condition": None,
                        "config": {
                            "name": "'${i}deploy${baseName}'",
                            "params": {
                                "storageName": "'${i}${baseName}'",
                                "location": "location",
                            },
                        },
                    },
                }
            },
        }
    )


def test_parse_loop_array():
    # given
    file_path = EXAMPLES_DIR / "loop/02-loop-array/main.bicep"

    # when
    result = BicepParser(file_path).json()

    # then
    assert_that(result).is_equal_to(
        {
            "outputs": {
                "out1": {
                    "type": "array",
                    "default": {
                        "loop_type": {
                            "type": "array",
                            "detail": {
                                "item_name": "i",
                                "array_name": "bicepVarArray",
                            },
                        },
                        "condition": None,
                        "config": {
                            "element": "i",
                        },
                    },
                }
            },
            "resources": {
                "storageArray": {
                    "type": "Microsoft.Storage/storageAccounts",
                    "api_version": "2021-06-01",
                    "config": {
                        "loop_type": {
                            "type": "array",
                            "detail": {
                                "item_name": "name",
                                "array_name": "storageNames",
                            },
                        },
                        "condition": None,
                        "config": {
                            "name": "'${name}${uniqueString(resourceGroup().id)}'",
                            "location": "location",
                            "sku": {
                                "name": "'Standard_LRS'",
                            },
                            "kind": "'Storage'",
                        },
                    },
                },
                "parentResources": {
                    "type": "Microsoft.Example/examples",
                    "api_version": "2020-06-06",
                    "config": {
                        "loop_type": {
                            "type": "array",
                            "detail": {
                                "item_name": "parent",
                                "array_name": "parents",
                            },
                        },
                        "condition": None,
                        "config": {
                            "name": "parent.name",
                            "properties": {
                                "children": {
                                    "loop_type": {
                                        "type": "array",
                                        "detail": {
                                            "item_name": "child",
                                            "array_name": "parent.children",
                                        },
                                    },
                                    "condition": None,
                                    "config": {
                                        "name": "child.name",
                                        "setting": "child.settingValue",
                                    },
                                }
                            },
                        },
                    },
                },
            },
            "modules": {
                "sqlFirewallRules": {
                    "type": "local",
                    "detail": {
                        "full": "sql-firewall-rule.bicep",
                        "path": "sql-firewall-rule.bicep",
                    },
                    "config": {
                        "loop_type": {
                            "type": "array",
                            "detail": {
                                "item_name": "firewallRules",
                                "array_name": "sqlLogicalServer.firewallRules",
                            },
                        },
                        "condition": None,
                        "config": {
                            "name": "'sqlFirewallRule-${uniqueString(sqlLogicalServer.name)}'",
                            "params": {
                                "sqlFirewallRule": "firewallRules",
                                "sqlServerName": "sqlLogicalServer.name",
                            },
                        },
                    },
                }
            },
        }
    )


def test_parse_loop_array_index():
    # given
    sub_dir_path = EXAMPLES_DIR / "loop/03-loop-array-index"
    file_path = sub_dir_path / "main.bicep"
    expected_result = json.loads((sub_dir_path / "result.json").read_text())

    # when
    result = BicepParser(file_path).json()

    # then
    assert_that(result).is_equal_to(expected_result)
