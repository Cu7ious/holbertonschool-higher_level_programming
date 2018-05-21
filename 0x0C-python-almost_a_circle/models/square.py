#!/usr/bin/python3
""" Module contains the `Square` class
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """ The `Square` class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ The constructor of the `Square` class

        Attrs:
            size: a size of a squareç
            x: a top padding
            y: a bottom padding
            id: optional id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Prints the instance in human readable format
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                self.width)
