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
        self.width = width
        self.height = height

    def __str__(self):
        """
        Prints the rectangle represented by the combinations of
        the `#` character.
        """
        result = ""

        if self.__height is 0 or self.__width is 0:
            return result

        for i in range(0, self.__height):
            result += "{:s}".format(self.__width * "#")

            if i + 1 is not self.__height:
                result += "\n"

        return result

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

    def area(self):
        """
        Computes the area of a rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Computes the perimeter of a rectangle
        """
        if self.__height is 0 or self.__width is 0:
            return 0

        return self.__height * 2 + self.__width * 2
