#!/usr/bin/python3


def max_integer(my_list=[]):
    """Finds the biggest integer of a list."""

    my_list.sort()

    return my_list[-1]
