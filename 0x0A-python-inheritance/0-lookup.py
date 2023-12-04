#!/usr/bin/python3
"""
Module Name: 0-lookup

Description: This module defines a function `lookup`.
Check the function's documentation for details.
"""


def lookup(obj):
    """
    Returns a list of an object's attributes and methods

    Parameters:
    - obj: An object
    """

    return dir(obj)
