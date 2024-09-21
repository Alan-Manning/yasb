import json
from typing import Any

# from .bar import BAR_DEFAULTS, BAR_SCHEMA
# from .config import CONFIG_SCHEMA
##############################################################################################################################################################
BAR_DEFAULTS = {
    "enabled": True,
    "screens": ["*"],
    "class_name": "yasb-bar",
    "alignment": {"position": "top", "center": False},
    "blur_effect": {
        "enabled": False,
        "dark_mode": False,
        "acrylic": False,
        "round_corners": False,
        "border_color": "System",
    },
    "window_flags": {"always_on_top": False, "windows_app_bar": False},
    "dimensions": {"width": "100%", "height": 30},
    "padding": {"top": 0, "left": 0, "bottom": 0, "right": 0},
    "widgets": {"left": [], "center": [], "right": []},
}

BAR_SCHEMA = {
    "type": "dict",
    "required": True,
    "schema": {
        "enabled": {
            "type": "boolean",
            "required": True,
            "default": BAR_DEFAULTS["enabled"],
        },
        "screens": {
            "type": "list",
            "schema": {"type": "string"},
            "default": BAR_DEFAULTS["screens"],
        },
        "class_name": {"type": "string", "default": BAR_DEFAULTS["class_name"]},
        "alignment": {
            "type": "dict",
            "schema": {
                "position": {
                    "type": "string",
                    "allowed": ["top", "bottom"],
                    "default": BAR_DEFAULTS["alignment"]["position"],
                },
                "center": {
                    "type": "boolean",
                    "default": BAR_DEFAULTS["alignment"]["center"],
                },
            },
            "default": BAR_DEFAULTS["alignment"],
        },
        "blur_effect": {
            "type": "dict",
            "schema": {
                "enabled": {
                    "type": "boolean",
                    "default": BAR_DEFAULTS["blur_effect"]["enabled"],
                },
                "dark_mode": {
                    "type": "boolean",
                    "default": BAR_DEFAULTS["blur_effect"]["dark_mode"],
                },
                "acrylic": {
                    "type": "boolean",
                    "default": BAR_DEFAULTS["blur_effect"]["acrylic"],
                },
                "round_corners": {
                    "type": "boolean",
                    "default": BAR_DEFAULTS["blur_effect"]["round_corners"],
                },
                "border_color": {
                    "type": "string",
                    "default": BAR_DEFAULTS["blur_effect"]["border_color"],
                },
            },
            "default": BAR_DEFAULTS["blur_effect"],
        },
        "window_flags": {
            "type": "dict",
            "schema": {
                "always_on_top": {
                    "type": "boolean",
                    "default": BAR_DEFAULTS["window_flags"]["always_on_top"],
                },
                "windows_app_bar": {
                    "type": "boolean",
                    "default": BAR_DEFAULTS["window_flags"]["windows_app_bar"],
                },
            },
            "default": BAR_DEFAULTS["window_flags"],
        },
        "dimensions": {
            "type": "dict",
            "schema": {
                "width": {
                    "anyof": [
                        {
                            "type": "string",
                            "minlength": 2,
                            "maxlength": 4,
                            "regex": "\\d+%",
                        },
                        {"type": "integer", "min": 0},
                    ],
                    "default": BAR_DEFAULTS["dimensions"]["width"],
                },
                "height": {
                    "type": "integer",
                    "min": 0,
                    "default": BAR_DEFAULTS["dimensions"]["height"],
                },
            },
            "default": BAR_DEFAULTS["dimensions"],
        },
        "padding": {
            "type": "dict",
            "schema": {
                "top": {"type": "integer", "default": BAR_DEFAULTS["padding"]["top"]},
                "left": {"type": "integer", "default": BAR_DEFAULTS["padding"]["left"]},
                "bottom": {
                    "type": "integer",
                    "default": BAR_DEFAULTS["padding"]["bottom"],
                },
                "right": {
                    "type": "integer",
                    "default": BAR_DEFAULTS["padding"]["right"],
                },
            },
            "default": BAR_DEFAULTS["padding"],
        },
        "widgets": {
            "type": "dict",
            "schema": {
                "left": {
                    "type": "list",
                    "schema": {"type": "string"},
                    "default": BAR_DEFAULTS["widgets"]["left"],
                },
                "center": {
                    "type": "list",
                    "schema": {"type": "string"},
                    "default": BAR_DEFAULTS["widgets"]["center"],
                },
                "right": {
                    "type": "list",
                    "schema": {"type": "string"},
                    "default": BAR_DEFAULTS["widgets"]["right"],
                },
            },
            "default": BAR_DEFAULTS["widgets"],
        },
    },
    "default": BAR_DEFAULTS,
}
CONFIG_SCHEMA = {
    "watch_config": {"type": "boolean", "default": True},
    "watch_stylesheet": {
        "type": "boolean",
        "default": True,
    },
    "debug": {
        "type": "boolean",
        "default": False,
        "required": False,
    },
    "komorebi": {
        "type": "dict",
        "schema": {
            "start_command": {
                "type": "string",
                "required": False,
            },
            "stop_command": {
                "type": "string",
                "required": False,
            },
            "reload_command": {
                "type": "string",
                "required": False,
            },
        },
        "default": {
            "start_command": "komorebic start --whkd",
            "stop_command": "komorebic stop --whkd",
            "reload_command": "komorebic reload-configuration",
        },
    },
    "bars": {
        "type": "dict",
        "keysrules": {"type": "string"},
        "valuesrules": BAR_SCHEMA,
        "default": {"yasb-bar": BAR_DEFAULTS},
    },
    "widgets": {
        "type": "dict",
        "keysrules": {
            "type": "string",
        },
        "valuesrules": {"type": ["string", "dict"]},
        "default": {},
    },
}
##############################################################################################################################################################

schema_dict: dict[str, Any] = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "$ref": "#/definitions/config",
    "definitions": {},
}

schema_dict["definitions"]["config"] = {
    "type": "object",
    "title": "config",
    "description": "main config for yasb.",
    "additionalProperties": False,
    "properties": {},
}


def add_definition(
    schema: dict[str, Any], definition_name: str, config_dict_to_add: dict[str, Any]
) -> dict[str, Any]:
    """Add a definition to the schema_dict."""

    # if schema["definitions"][definition_name]["default"]:

    schema["definitions"][definition_name] = {
        "type": "object",
        "title": definition_name,
        "description": f"Settings for {definition_name}",
        "additionalProperties": False,
        "properties": {},
    }
    print(config_dict_to_add["default"])
    for key, val in config_dict_to_add["default"].items():
        print(key)
        print(val)
        schema["definitions"][definition_name]["properties"][key] = {
            "title": key,
            "default": val,
        }

    return schema


for config_key, config_inner in CONFIG_SCHEMA.items():

    if config_inner["type"] != "dict":
        schema_dict["definitions"]["config"]["properties"][config_key] = {
            "type": config_inner["type"],
            "title": config_key,
            "default": config_inner["default"],
        }
    else:
        schema_dict["definitions"]["config"]["properties"][config_key] = {
            "$ref": f"#/definitions/{config_key}",
        }

        add_definition(schema_dict, config_key, config_inner)


with open("schema.json", "w", encoding="utf-8") as f:
    json.dump(schema_dict, f, ensure_ascii=False, indent=4)