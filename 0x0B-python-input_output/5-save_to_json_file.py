#!/usr/bin/python3
"""
Module Name: 5-save_to_json_file

Description: This module defines a function `save_to_json_file`.
Check the function's documentation for details.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using JSON representation.

    Parameters:
    - my_obj: An object
    - filename: The name of a file
    """

    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
