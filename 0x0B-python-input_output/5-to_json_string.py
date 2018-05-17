#!/usr/bin/python3
import json
"""
Contains the `to_json_string` function
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)

    Args:
        my_obj: an object to serialize
    """
    return json.dumps(my_obj)
