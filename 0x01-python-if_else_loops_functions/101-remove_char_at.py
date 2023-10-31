#!/usr/bin/python3
"""Remove a character from a string"""


def remove_char_at(str, n):
    str_list = list(str)
    if n >= 0 and n <= len(str) - 1:
        str_list.pop(n)
    new_str = "".join(str_list)
    return new_str
