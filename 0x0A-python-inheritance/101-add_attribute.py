#!/usr/bin/python3
"""
Defines the `add_attribute` function
"""


def add_attribute(obj, name, val):
    """
    add_attribute - adds property (if possible) to an instance of a class
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, name, val)
    else:
        raise TypeError("can't add new attribute")
