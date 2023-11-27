#!/usr/bin/python3
"""
Module Name: 0-rectangle

Description: This module contains a class `Rectangle`
that defines a rectangle
"""


class Rectangle:
    """
    Rectangle: Defines a rectangle

    Instance Attributes:
    - width (int): The width of a rectangle
    - height (int): The height of a rectangle

    Class Attributes:
    - number_of_instances (int): The number of instances
    - print_symbol: The print symbol to use for printing a rectangle

    Properties:
    - width (int): A property representing the width
    - height (int): A property representing the height

    Instance Methods:
    - area() -> int: Calculate the area of the rectangle
    - perimeter() -> int: Calculate the perimiter of the rectangle

    Static Methods:
    - bigger_or_equal() -> Rectangle: Returns the biggest rectangle
    based on the area

    Class Methods:
    - square() -> Rectangle: Returns a new Rectangle instance
    with width == height == size
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes attributes"""
        self.width = width
        self.height = height

        type(self).number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance
        with width == height == size"""

        return Rectangle(size, size)

    def __str__(self):
        """Prints the rectangle filled with #"""

        rectangle = []

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append(str(self.print_symbol))
            if i != self.__height - 1:
                rectangle.append("\n")

        return "".join(rectangle)

    def __repr__(self):
        """Returns a string representation of the rectangle"""

        return ("Rectangle(" + str(self.__width) + ", "
                + str(self.__height) + ")")

    def __del__(self):
        """Prints a message when an instance is deleted"""

        type(self).number_of_instances -= 1
        print("Bye rectangle...")
