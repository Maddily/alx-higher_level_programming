#!/usr/bin/python3
"""
Module Name: 4-inherits_from

Decription: This module defines a function `inherits_from`.
Check the function's documentation for details.
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherits
    (directly or indirectly) from the specified class.

    Parameters:
    - obj: An object
    - a_class: A class

    Return:
    - True: If the object is an instance of a class that inherits
    from the specified class.
    - False: If the object isn't an instance of a class that inherits
    from the specified class.
    """

    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    return False
