#!/usr/bin/python3
"""
Module Name: 0-add_integer

Description:
    This module contains a function that adds two numbers

Functions:
    - add_integer: Adds two numbers
"""


def add_integer(a, b=98):
    """
    Adds two numbers

    Parameters:
    - a: The first number.
    - b: The second number.

    Returns:
    The sum of the two numbers.
    """

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    if (
            not isinstance(a, int)
            and not isinstance(a, float)
    ):
        raise TypeError("a must be an integer")

    if (
            not isinstance(b, int)
            and not isinstance(b, float)
    ):
        raise TypeError("b must be an integer")

    if isinstance(a, bool):
        raise TypeError("a must be an integer")

    if isinstance(b, bool):
        raise TypeError("b must be an integer")

    return a + b
