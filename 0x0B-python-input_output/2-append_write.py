#!/usr/bin/python3
"""
Module Name: 2-append_write

Description: This module defines a function `append_write`.
Check the function's documentation for details.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file and returns
    the number of characters added.

    Parameters:
    - filename: The name/path of a file
    - text: The text to be appended
    """

    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
