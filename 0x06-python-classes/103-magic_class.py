#!/usr/bin/python3
"""Define a Python class called MagicClass"""

import math
"""The 'math' module provides mathematical functions and constants"""


class MagicClass:
    """A class representing a magical circle."""

    def __init__(self, radius=0):
        """Initialize a new MagicClass instance"""

        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """Calculate the area of the magical circle"""

        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate the circumference of the magical circle"""

        return 2 * math.pi * self.__radius
