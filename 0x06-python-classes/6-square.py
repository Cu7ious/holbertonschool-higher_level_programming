#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """The class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor of the Square class"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """The __size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """The __size setter"""
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Returns the size of the square"""
        return self.__size ** 2

    @property
    def position(self):
        """The __position getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """The __position setter"""
        if isinstance(value, tuple) is False or len(value) is not 2:
            raise TypeError("Position must be a tuple of 2 positive integers")

        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("Position must be a tuple of 2 positive integers")

        if value[0] < 0 or value[1] < 0:
            raise TypeError("Position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """Prints the square with the character #, padded with spaces
        into the stdout."""
        if self.size is 0:
            print()
        else:
            for j in range(0, self.position[1]):
                print("{:s}".format(" " * (self.position[0] + self.size)))

            for i in range(0, self.size):
                print("{:s}".format(" " * self.position[0] + "#" * self.size))
