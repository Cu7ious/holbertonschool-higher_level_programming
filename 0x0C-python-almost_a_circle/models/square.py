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
        self.size = size

    def __str__(self):
        """ Prints the instance in human readable format
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """ updates the arguments of the instance

        Args:
            *args: variadic arguments list
            **kwargs: double pointer to a dictionary in key:val format
        """
        if len(args):
            for c, arg in enumerate(args):
                if c is 0:
                    self.id = arg
                if c is 1:
                    self.size = arg
                if c is 2:
                    self.x = arg
                if c is 3:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ returns the dictionary representation
            of a Square"""
        res = {}
        for key, val in self.__dict__.items():
            key = key.replace("_Rectangle__", "")
            key = "size" if key == "width" else key

            if key == "height":
                continue

            res[key] = val

        return res

    @property
    def size(self):
        """ size getter
        """
        return self.width

    @size.setter
    def size(self, val):
        """ size setter
        """
        self.width = val
        self.height = val
