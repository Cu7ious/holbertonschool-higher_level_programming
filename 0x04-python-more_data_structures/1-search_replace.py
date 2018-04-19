#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another in a new list."""

    n = my_list.count(search)
    result = my_list.copy()

    if (n is not 0):
        for i in range(0, n):
            result[result.index(search)] = replace

    return result
