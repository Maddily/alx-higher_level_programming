#!/usr/bin/python3
"""
This module contains a function that finds a peak
in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""

    if not list_of_integers:
        return None

    length = len(list_of_integers)

    for i in range(length):
        if (
            i == 0
            and i + 1 in range(length)
            and list_of_integers[i] > list_of_integers[i + 1]
        ):
            return list_of_integers[i]

        if (
            i - 1 in range(length)
            and list_of_integers[i] > list_of_integers[i - 1]
            and i + 1 in range(length)
            and list_of_integers[i] > list_of_integers[i + 1]
        ):
            return list_of_integers[i]

    return list_of_integers[i]
