#!/usr/bin/python3
""" Module contains the `Base` class
"""


class Base:
    """ The `Base` class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor of the `Base` class

        Args:
            id: the uniqe id
        """
        if id is None:
            Base.__nb_objects += 1
            id = self.__nb_objects

        self.id = id
