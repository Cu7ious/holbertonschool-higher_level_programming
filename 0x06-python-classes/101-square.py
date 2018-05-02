#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """The class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializer function for a Square.

        Args:
            size (int): Size of the Square.
            position (tuple): Position of the Square.
        """
        self.size = size
        self.position = position

    def __str__(self):
        self.my_print(True)
        return ""

    @property
    def size(self):
        """ Gets private __size attribute.

        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets a new value for __size attribute.

        Args:
            value (int): The value of the new size.
        """
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Gets private __position attribute.

        Returns:
            The position of the Square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the value for the __position attribute.

        Args:
            value (int): The value of the new position.
        """
        if isinstance(value, tuple) is False or len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")

        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Calculates the area of the Square.

        Returns:
            The area of the Square.
        """
        return self.size ** 2

    def my_print(self, is__str__=False):
        """Prints the square with the character #, padded with spaces."""
        if self.size is 0:
            if is__str__ is False:
                print()
        else:
            for j in range(0, self.position[1]):
                print()

            for i in range(0, self.size):
                if is__str__ is True:
                    if i + 1 is self.size:
                        print(" " * self.position[0] + "#" * self.size, end="")
                    else:
                        print(" " * self.position[0] + "#" * self.size)
                else:
                    print(" " * self.position[0] + "#" * self.size)
