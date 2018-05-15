#!/usr/bin/python3
"""
Module that contains the `is_kind_of_class` function
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class

    Args:
        obj: the object to check
        a_class: a class to check the obj on
    """
    return isinstance(obj, a_class)
