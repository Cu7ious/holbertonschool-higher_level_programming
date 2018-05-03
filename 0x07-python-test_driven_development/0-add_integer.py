#!/usr/bin/python3
"""This module creates the function that adds 2 integers"""


def add_integer(a, b=98):
    """Adds 2 integers."""

    if not isinstance(a, int) or not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) or not isinstance(b, float):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return a + b
