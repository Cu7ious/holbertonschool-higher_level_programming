#!/usr/bin/python3
"""
Module that contains the `` function
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class

    Args:
        obj: the object to check
        a_class: a class to check the obj on

    Return: bool
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
