#!/usr/bin/python3
"""
Module Name: 3-is_kind_of_class

Description: This module defines a function `is_kind_of_class`.
Check the function's documentation for details.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of the specified class,
    or if it's an instance of a class that inherits from the specified class.

    Parameters:
    - obj: An object
    - a_class: A class

    Return:
    - True if the object is an instance of the specified class
    - False if the object isn't an instance of the specified class
    """

    if isinstance(obj, a_class):
        return True
    return False
