##!/usr/bin/python3
"""
Say my name - say_my_name function.
Accepts: two strings, first_name & last_name
It will print out a string with the two input strings
Checks: type first_name & last_name is string
"""


def say_my_name(first_name, last_name=""):
        """
        say_my_name: prints a message with the input names
        """

        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")

        if not isinstance(last_name, str):
            raise TypeError("last_name must be a string")

        print("My name is {:s} {:s}".format(first_name, last_name))
