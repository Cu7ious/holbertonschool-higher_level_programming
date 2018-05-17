#!/usr/bin/python3
import json
"""
Contains the `` function
"""


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation

    Args:
        my_obj: the Python object to serialize
        filename: a name of a file to write to
    """
    with open(filename, mode="w", encoding="utf-8") as a_file:
        a_file.write(json.dumps(my_obj))
