#!/usr/bin/python3
"""
Module Name: 3-to_json_string

Description: This module defines a function `to_json_string`.
Check the function's documentation for details.
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object.

    Parameters:
    - my_obj: An object
    """

    return json.dumps(my_obj)
