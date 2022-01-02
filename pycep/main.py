import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

from lark import Lark, Token, Transformer, Tree
from typing_extensions import Literal

LARK_GRAMMAR = (Path(__file__).parent / "bicep.lark").read_text()

BICEP_REGISTRY_PATTERN = re.compile(r"br:(?P<registry_name>\w+)\.azurecr\.io/(?P<path>[\w/]+):(?P<tag>[\w.\-]+)")
TEMPLATE_SPEC_PATTERN = re.compile(
    r"ts:(?P<sub_id>[\d\-]+)/(?P<rg_id>[\w._\-()]+)/(?P<name>[\w.\-]+):(?P<version>[\w.\-]+)"
)


class BicepToJson(Transformer):
    def start(self, args: List) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        for arg in args:
            for key, value in arg.items():
                result.setdefault(key, {})[value["__name__"]] = value["__attrs__"]

        return result

    ####################
    #
    # elements
    #
    ####################

    def param(self, args: Tuple[Token, Token, Optional[Token]]):
        name, data_type, default = args
        return {
            "parameters": {
                "__name__": name,
                "__attrs__": {
                    "type": data_type,
                    "default": default,
                },
            }
        }

    def var(self, args: Tuple[Token, Token]):
        name, value = args

        return {
            "variables": {
                "__name__": name,
                "__attrs__": {
                    "value": value,
                },
            }
        }

    def output(self, args: Tuple[Token, Token, Token]):
        name, data_type, value = args
        return {
            "outputs": {
                "__name__": name,
                "__attrs__": {
                    "type": data_type,
                    "default": value,
                },
            }
        }

    def resource(self, args: Tuple[str, Dict[str, str], Dict[str, Any]]):
        name, type_api_pair, config = args

        if config.get("loop_type"):
            pass

        return {
            "resources": {
                "__name__": name,
                "__attrs__": {
                    **type_api_pair,
                    "config": config,
                },
            }
        }

    def module(self, args):
        name, path, config = args
        return {
            "modules": {
                "__name__": name,
                "__attrs__": {
                    **path,
                    "config": config,
                },
            }
        }

    ####################
    #
    # element type extras
    #
    ####################

    def data_type(self, arg: Tuple[Token]) -> str:
        return str(arg[0])

    def type_api_pair(self, args: Tuple[Token, Token]) -> Dict[str, str]:
        type_name, api_version = args
        return {"type": str(type_name), "api_version": str(api_version)}

    def module_path(self, args: Tuple[Token]) -> Dict[str, Any]:
        file_path = str(args[0])[1:-1]

        if file_path.startswith("br:"):
            m = re.match(BICEP_REGISTRY_PATTERN, file_path)

            return {
                "type": "bicep_registry",
                "detail": {
                    "full": file_path[3:],
                    "registry_name": m.group("registry_name"),
                    "path": m.group("path"),
                    "tag": m.group("tag"),
                },
            }
        elif file_path.startswith("ts:"):
            m = re.match(TEMPLATE_SPEC_PATTERN, file_path)

            return {
                "type": "template_spec",
                "detail": {
                    "full": file_path[3:],
                    "subscription_id": m.group("sub_id"),
                    "resource_group_id": m.group("rg_id"),
                    "name": m.group("name"),
                    "version": m.group("version"),
                },
            }

        return {
            "type": "local",
            "detail": {
                "full": file_path,
                "path": file_path,
            },
        }

    ####################
    #
    # loops
    #
    ####################

    def loop(self, args: Tuple[Token, Token, Token]):
        loop_type, condition, config = args
        return {
            "loop_type": loop_type,
            "condition": condition,
            "config": config,
        }

    def loop_range(self, args: Tuple[Token, Token, Token]) -> Dict[str, Any]:
        idx_name, start_idx, count = args
        return {
            "type": "index",
            "detail": {
                "index_name": str(idx_name),
                "start_index": str(start_idx),
                "count": str(count),
            },
        }

    def loop_array(self, args: Tuple[Token, Token]) -> Dict[str, Any]:
        item_name, array_name = args
        return {
            "type": "array",
            "detail": {
                "item_name": str(item_name),
                "array_name": str(array_name),
            },
        }

    def loop_array_index(self, args: Tuple[Token, Token]) -> Dict[str, Any]:
        item_name, idx_name, array_name = args
        return {
            "type": "array",
            "detail": {
                "item_name": str(item_name),
                "index_name": str(idx_name),
                "array_name": str(array_name),
            },
        }

    ####################
    #
    # data types
    #
    ####################

    def array(self, args: List[Union[bool, int, Token]]) -> List[Union[bool, int, str]]:
        result = [item.value if isinstance(item, Token) else item for item in args]
        return result

    def object(self, args: List[Tuple[str, Any]]) -> Dict[str, Any]:
        return dict(args)

    def pair(self, args):
        key, value = args
        return (key, value.value if isinstance(value, Token) else value)

    def key(self, arg: Tuple[Token]) -> str:
        return str(arg[0])

    def int(self, arg: Tuple[Token]) -> int:
        return int(arg[0])

    def string(self, arg: Tuple[Token]) -> str:
        return str(arg[0])

    def multi_line_string(self, arg: Tuple[Token]):
        value = arg[0].value[3:-3]
        value = value[1:] if value.startswith("\n") else value
        return f"'{value}'"

    def true(self, _) -> Literal[True]:
        return True

    def false(self, _) -> Literal[False]:
        return False


class BicepParser:
    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path

        self.tree = self._create_tree()

    def _create_tree(self) -> Tree:
        content = self.file_path.read_text()
        lark_parser = Lark(grammar=LARK_GRAMMAR, parser="lalr", propagate_positions=True)

        return lark_parser.parse(content)

    def json(self) -> Dict[str, Any]:
        return BicepToJson().transform(self.tree)

    def print_tree(self) -> str:
        return self.tree.pretty()
