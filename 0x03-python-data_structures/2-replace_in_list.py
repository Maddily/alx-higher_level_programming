#!/usr/bin/python3
"""Replace an element at a given index in a list"""


def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list

    my_list[idx] = element
    return my_list
