#!/usr/bin/python3


class Rectangle:
    """
    Rectangle: class that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Constructor for the Rectangle class
        Args:
            width: the width of a rectangle
            height: the height of a rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        The `width` property getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        The `width` property setter
        """
        # if type(value) is not int:
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        The `height` property getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        The `height` property setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
