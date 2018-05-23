#!/usr/bin/python3
""" Module contains the `Rectangle` class
"""
from .base import Base


class Rectangle(Base):
    """ The `Rectangle` class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ The constructor of the `Rectangle` class

        Attrs:
            width: a width of a rectangle
            height: a height of a rectangle
            x: a top padding
            y: a bottom padding
            id: optional id
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """ Prints the instance in human readable format
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def area(self):
        """ Computes the area of a rectangle
        """
        return self.__height * self.__width

    def display(self):
        """ Displays the rectangle
        """
        for _ in range(self.y):
            print()

        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

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
            if "width" in kwargs:
                self.size = kwargs["width"]
            if "height" in kwargs:
                self.size = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ returns the dictionary representation
            of a Rectangle"""
        res = {}
        for key, val in self.__dict__.items():
            key = key.replace("_Rectangle__", "")
            res[key] = val

        return res

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        if type(val) is not int:
            raise TypeError("width must be an integer")

        if val <= 0:
            raise ValueError("width must be > 0")

        self.__width = val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        if type(val) is not int:
            raise TypeError("height must be an integer")

        if val <= 0:
            raise ValueError("height must be > 0")

        self.__height = val

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if type(val) is not int:
            raise TypeError("x must be an integer")

        if val < 0:
            raise ValueError("x must be >= 0")

        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        if type(val) is not int:
            raise TypeError("y must be an integer")

        if val < 0:
            raise ValueError("y must be >= 0")

        self.__y = val
