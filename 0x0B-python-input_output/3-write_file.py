#!/usr/bin/python3
"""
Contains the `write_file` function
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns
    the number of characters written

    Args:
        filename: the path to file to read+print
        nb_lines: number of lines to read
    """
    with open(filename, mode="w", encoding="utf-8") as a_file:
        return a_file.write(text)
