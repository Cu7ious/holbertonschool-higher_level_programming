#!/usr/bin/python3


def no_c(my_string):
    """Removes all characters c and C from a string."""

    result = ""

    for char in my_string:
        if char is "c" or char is "C":
            continue

        result += char

    return result
