#!/usr/bin/python3
"""Remove 'c' and 'C' from a string"""


def no_c(my_string):
    string_list = [my_string[i] for i in range(len(my_string))
                   if my_string[i] != "c" and my_string[i] != "C"]

    new_string = "".join(string_list)
    return new_string
