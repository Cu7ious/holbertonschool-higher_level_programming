#!/usr/bin/python3
"""
    This module creates the function that adds 2 integers

    add_integer(2, 2) # 4
"""


def add_integer(a, b=98):
    """
        Adds 2 integers.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
