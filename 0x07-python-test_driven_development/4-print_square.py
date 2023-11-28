#!/usr/bin/python3
"""
Module Name: 4-print_square

Description:
    This module contains a function that prints
    a square filled with the character `#`.

Functions:
    - print_square: Prints a square filled with
    the character `#`.
"""


def print_square(size):
    """
    Prints a square filled with the character `#`.

    Parameters:
    - size: The size of the square.
    """

    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
