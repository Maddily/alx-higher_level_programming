#!/usr/bin/python3
"""Find the largest integer in a list"""


def max_integer(my_list=[]):
    if not my_list:
        return None

    largest_int = my_list[0]
    for int in my_list[1:]:
        if int > largest_int:
            largest_int = int

    return largest_int
