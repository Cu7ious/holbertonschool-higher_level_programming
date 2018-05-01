#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    """Prints an integer."""
    try:
        print("{:d}".format(value))
        return True
    except Exception as err:
        print("Exception: {}".format(err.args[0]), file=stderr)
        return False
