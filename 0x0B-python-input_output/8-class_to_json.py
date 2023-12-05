#!/usr/bin/python3
"""
Module Name: 8-class_to_json

Description: This module defines a function `class_to_json`.
Check the function's documentation for details.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object.

    Parameters:
    - obj: An object (An instance of a class)
    """

    obj_attr = {attr: getattr(obj, attr) for attr in obj.__dict__
                if not callable(getattr(obj, attr))}

    return obj_attr
