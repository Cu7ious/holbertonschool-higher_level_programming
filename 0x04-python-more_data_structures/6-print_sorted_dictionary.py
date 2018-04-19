#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys."""

    sorted_keys = sorted(set(a_dictionary))

    for key in sorted_keys:
        print("{:s}: {}".format(key, a_dictionary[key]))
