#!/usr/bin/python3
import json
"""
Contains the `load_from_json_file` function
"""


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file

    Args:
        filename: the path to a file
    """
    with open(filename, mode="r", encoding="utf-8") as a_file:
        return json.loads(a_file.read())
