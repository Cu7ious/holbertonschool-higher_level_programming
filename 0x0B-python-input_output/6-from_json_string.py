#!/usr/bin/python3
import json
"""
Contains the `from_json_string` function
"""


def from_json_string(my_str):
    """
    function that returns an object (Python data structure)
    represented by a JSON string

    Args:
        my_str: an object to serialize
    """

    return json.loads(my_str)
