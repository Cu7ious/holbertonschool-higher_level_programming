#!/usr/bin/python3
"""
    This module contains the say_my_name function.
    It accepts two strings with the second string given a default string.
    It will print out a string with the two input strings
    Checks whether or not the inputs are strings.
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name: Takes up to two input strings and printsout a message
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
