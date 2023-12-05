#!/usr/bin/python3
"""
Module Name: 0-read_file

Description: This module defines a function `read_file`.
Check the function's documentation for details.
"""


def read_file(filename=""):
    """
    Reads a text file and prints it to stdout.

    Parameters:
    - filename: The name/path of a file
    """

    if not filename:
        return
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
