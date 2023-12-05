#!/usr/bin/python3
"""
Module Name: 100-append_after

Description: This module defines a function `append_after`.
Check the function's documentation for details.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file,
    after each line containing a specific string.

    Parameters:
    - filename: The name of a file
    - search_string: A string for which to be searched
    - new_string: A string to be inserted after each line
        containing `search_string`
    """

    with open(filename, "r+", encoding="utf-8") as file:
        lines = file.readlines()
        file.seek(0)

        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
