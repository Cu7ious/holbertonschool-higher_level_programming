#!/usr/bin/python3
"""
Contains the `number_of_lines` function
"""


def number_of_lines(filename=""):
    """
    Returns the number of lines of a text file

    Args:
        filename: thg name of the file
    """
    with open(filename, mode="r") as a_file:
        return len(a_file.readlines())
