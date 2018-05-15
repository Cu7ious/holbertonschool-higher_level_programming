#!/usr/bin/python3
"""
Module that contains the `is_same_class` function
"""


def is_same_class(obj, a_class):
    """
    checks if the object is exactly an instance of the specified class

    Args:
        obj: 
        a_class: 
    """
    return type(obj) is a_class
