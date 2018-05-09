#!/usr/bin/python3
"""
print_square function.
Args: `size` int
Prints: square filled with `#` char of size `size`.
"""


def print_square(size):
        """
        print_square: prints a filled with `#` char of size `size`.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        for i in range(size):
            for j in range(size):
                print("#", end="")

            print()
