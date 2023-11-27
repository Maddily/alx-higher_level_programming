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
    width (int): A property representing the width
    height (int): A property representing the height
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

        self.__height = value

    @property
    def height(self):
        """Retrieves `height`"""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets `height`"""

        if not isinstance(value, int):
            TypeError("height must be an integer")

        if value < 0:
            ValueError("height must be >= 0")

        self.__height = value
