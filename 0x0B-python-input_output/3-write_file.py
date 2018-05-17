#!/usr/bin/python3
"""
Contains the `write_file` function
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns
    the number of characters written

    Args:
        filename: the path to file to write to
        text: a text to write
    """
    with open(filename, mode="w", encoding="utf-8") as a_file:
        return a_file.write(text)
