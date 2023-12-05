#!/usr/bin/python3
"""
Module Name: 6-load_from_json_file

Description: This module defines a function `load_from_json_file`.
Check the function's documentation for details.
"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Parameters:
    - filename: The name of a file
    """

    with open(filename, encoding="utf-8") as file:
        return json.loads(file.read())
