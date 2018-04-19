#!/usr/bin/python3


def uniq_add(my_list=[]):
    """Makes the addition of all unique integers in a list
        (only one time each integer)."""

    result = 0
    uniq = set(my_list)

    for x in uniq:
        result += x

    return result
