#!/usr/bin/python3
"""
Contains the `read_lines` function
"""


def read_lines(filename="", nb_lines=0):
    """
    Reads n lines of a text file (UTF8) and prints it to stdout

    Args:
        filename: the path to file to read+print
        nb_lines: number of lines to read
    """
    with open(filename, mode="r", encoding="utf-8") as a_file:
        if nb_lines <= 0:
            print(a_file.read(), end="")
        else:
            lines = a_file.readlines()

            counter = 0
            for line in lines:
                if nb_lines == counter:
                    break

                print(line, end="")

                counter += 1
