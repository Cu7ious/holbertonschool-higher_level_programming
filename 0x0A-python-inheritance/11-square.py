#!/usr/bin/python3
"""
Contains the `Square` class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    The `Square` class
    """

    def __init__(self, size):
        """
        The constructor of the `Rectangle` class
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        Print magic method
        """
        return "[Square] {0:d}/{0:d}".format(self.__size)

    def area(self):
        """
        Returns the area of the square
        """
        return self.__size * self.__size
