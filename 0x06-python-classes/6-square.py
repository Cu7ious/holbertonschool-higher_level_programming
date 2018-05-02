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
            return

        if value < 0:
            raise ValueError("size must be >= 0")
            return

        self.__size = value

    def area(self):
        """Returns the size of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #, padded with spaces
        into the stdout."""
        if self.size is 0:
            print()
        else:
            if self.position[1] > 0:
                for j in range(0, self.position[1]):
                    # print()
                    print(" " * (self.position[0] + self.size))

            for i in range(0, self.size):
                print(" " * self.position[0] + "#" * self.size)

    @property
    def position(self):
        """The __position getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """The __position setter"""
        if isinstance(value, tuple) is not True and len(value) is not 2:
            raise TypeError("Position must be a tuple of 2 positive integers")
            return

        self.__position = value
