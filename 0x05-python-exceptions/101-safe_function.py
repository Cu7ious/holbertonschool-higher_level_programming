#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    """Executes a function safely."""

    try:
        result = fct(*args)
        return result
    except Exception as exc:
        print("Exception: {}".format(exc.args[0]), file=stderr)
        return None
