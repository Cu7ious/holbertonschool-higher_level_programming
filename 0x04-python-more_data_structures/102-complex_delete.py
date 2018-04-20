#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary."""

    if (value in a_dictionary.values() is False):
        return a_dictionary

    keys_to_del = []

    for item in a_dictionary.items():
        if item[1] == value:
            keys_to_del.append(item[0])

    for key in keys_to_del:
        del a_dictionary[key]

    return a_dictionary
