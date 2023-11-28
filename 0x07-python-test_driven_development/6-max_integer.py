#!/usr/bin/python3
"""
Module Name: 6-max_integer

Description:
    This module contains a function that
    finds the largest integer in a list.

Functions:
    - max_integer: Finds the largest integer in a list.
"""


def max_integer(list=[]):
    """
    Find and return the max integer in a list of integers.
    If the list is empty, the function returns None.

    Parameters:
    - list: The list to be searched.

    Returns:
    the integer or None
    """

    if len(list) == 0:
        return None
    largest_integer = list[0]
    i = 1
    while i < len(list):
        if list[i] > largest_integer:
            largest_integer = list[i]
        i += 1
    return largest_integer
