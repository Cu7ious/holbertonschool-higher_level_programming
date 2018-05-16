#!/usr/bin/python3
"""
Contains the ``MyInt class
"""


class MyInt(int):
    def __init__(self, val):
        """
        The constrcuctor.
        Creates new public property, identical to self

        Args:
            self: the reference to a class/instance
            val: a value
        """
        self.val = val

    def __eq__(self, other):
        """
        `Is equal` magic method

        Args:
            self: the reference to a class/instance
            other: a value of other instance
        """
        return not self.val == other

    def __ne__(self, other):
        """
        `Is not equal` magic method

        Args:
            self: the reference to a class/instance
            other: a value of other instance
        """
        return not self.__eq__(other)
