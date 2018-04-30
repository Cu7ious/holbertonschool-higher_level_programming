#!/usr/bin/python3


def safe_print_division(a, b):
    """Divides 2 integers and prints the result."""

    c = None

    try:
        c = a / b
    except(ZeroDivisionError):
        pass
    finally:
        print("Inside result: {}".format(c))
        return c
