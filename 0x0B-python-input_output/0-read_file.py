#!/usr/bin/python3
"""
Contains the `read_file` function
"""


def read_file(filename=""):
    """
    reads a text file (UTF8) and prints it to stdout

    Args:
        filename: the path to file to read+print
    """
    with open(filename, mode="r", encoding="utf-8") as a_file:
        print(a_file.read(), end="")
