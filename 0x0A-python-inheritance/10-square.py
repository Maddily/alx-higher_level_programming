#!/usr/bin/python3
"""
Module Name: 10-square

Description: This module defines a class `Square`
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Defines a square

    Attributes:
    - size: A private instance attribute for the size of a square
    """

    def __init__(self, size):
        """Initializes"""

        self.__size = size
        Rectangle.integer_validator(self, "size", self.__size)

    def area(self):
        """Returns the area of the square"""

        return self.__size ** 2

    def __str__(self):
        """Returns a string representation of a rectangle object"""

        return f"[Rectangle] {self.__size}/{self.__size}"
