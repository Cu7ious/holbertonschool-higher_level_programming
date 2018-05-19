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
            x: the x coordinate
            y: the y coordinate
            id: optional id
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        self.__width = val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        self.__height = val

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        self.__y = val
