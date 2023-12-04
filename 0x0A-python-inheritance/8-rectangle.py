#!/usr/bin/python3
"""
Module Name: 8-rectangle

Description: This module defines a class `Rectangle`.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Defines a rectangle

    Instance Attributes:
    - width: A positive integer
    - height: A positive integer
    """

    def __init__(self, width, height):
        """Initializes"""

        self.__width = width
        self.__height = height

        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
