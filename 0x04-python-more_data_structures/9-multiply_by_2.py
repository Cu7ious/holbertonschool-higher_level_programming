#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied by 2."""

    result = {}

    for key, val in a_dictionary.items():
        result[key] = val * 2

    return result
