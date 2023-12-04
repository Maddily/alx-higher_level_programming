#!/usr/bin/python3
"""
Module Name: 7-base_geometry

Description: This module defines a class `BaseGeometry`.
"""


class BaseGeometry():
    """
    Defines a function `area`

    Public Instance Methods:
    - area(): Raises an exception
    """

    def area(self):
        """Raises an exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates `value`.

        Parameters:
        - name: A string
        - value: A value of an unknown type
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
