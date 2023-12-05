#!/usr/bin/python3
"""
Module Name: 1-write_file

Description: This module defines a function `write_file`.
Check the function's documentation for details.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and returns
    the number of characters written.

    Parameters:
    - filename: The name of a file
    - text: The text to be written
    """

    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
