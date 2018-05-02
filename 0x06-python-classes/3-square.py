#!/usr/bin/python3


class Square:
    def __init__(self, num=None):

        if num:
            if isinstance(num, int) is not True:
                raise TypeError("size must be an integer")
                return

            if num < 0:
                raise ValueError("size must be >= 0")
                return

            self.__size = num

    def area(self):
        return self.__size ** 2
