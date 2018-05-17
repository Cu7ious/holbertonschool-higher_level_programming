#!/usr/bin/python3
"""
Contains the `append_write` function
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)
    and returns the number of characters added

    Args:
        filename: the path to file to open
        text: the content to append
    """
    with open(filename, mode="a", encoding="utf-8") as a_file:
        return a_file.write(text)
