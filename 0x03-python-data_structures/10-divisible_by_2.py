#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list."""

    result = []

    for el in my_list:
        if el % 2 is 0:
            result.append(True)
        else:
            result.append(False)

    return result
