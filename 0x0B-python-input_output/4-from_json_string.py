#!/usr/bin/python3
"""
Module Name: 4-from_json_string

Description: This module defines a function `from_json_string`.
Check the function's documentation for details.
"""
import json


def from_json_string(my_str):
    """
    Returns an object represented by a JSON string.

    Parameters:
    - my_str: A JSON string
    """

    return json.loads(my_str)
