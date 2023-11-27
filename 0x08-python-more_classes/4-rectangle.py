#!/usr/bin/python3
"""
Module Name: 0-rectangle

Description: This module contains a class `Rectangle`
that defines a rectangle
"""


class Rectangle:
    """
    Rectangle: Defines a rectangle

    Attributes:
    - width (int): The width of a rectangle
    - height (int): The height of a rectangle

    Properties:
    - width (int): A property representing the width
    - height (int): A property representing the height

    Methods:
    - area() -> int: Calculate the area of the rectangle
    - perimeter() -> int: Calculate the perimiter of the rectangle
    """

    def __init__(self, width=0, height=0):
        """Initializes attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves `width`"""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets `width`"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Retrieves `height`"""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets `height`"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimiter of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Prints the rectangle filled with #"""

        rectangle = []

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append("#")
            if i != self.__height - 1:
                rectangle.append("\n")

        return "".join(rectangle)

    def __repr__(self):
        """Returns a string representation of the rectangle"""

        return ("Rectangle(" + str(self.__width) + ", "
                + str(self.__height) + ")")
