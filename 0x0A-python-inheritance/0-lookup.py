#!/usr/bin/python3
"""
Module that contains the lookup function
"""


def lookup(obj):
    """
    Method that returns all of the available attributes + methods of an object

    Args:
        obj: the object to look up
    """

    result = []

    for el in dir(obj):
        result.append(el)

    return result
