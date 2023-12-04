#!/usr/bin/python3
"""
Module Name: 101-add_attribute

Description: This module defines a function `add_attribute`.
"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object, if possible

    Parameters:
    - obj: An object
    - attr: The name of the attribute
    - value: The value of the attribute
    """

    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
