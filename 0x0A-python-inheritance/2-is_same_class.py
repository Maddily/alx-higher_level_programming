#!/usr/bin/python3
"""
Module Name: 2-is_same_class

Description: This module defines a function `is_same_class`.
Check the function's documentation for details.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.

    Parameters:
    - obj: An object
    - a_class: A class

    Return:
    - True if the object is exactly an instance of the specified class
    - False if the object isn't exactly an instance of the specified class
    """

    if type(obj) is a_class:
        return True
    return False
