#!/usr/bin/python3
"""Display all integers of a list, sorted in descending order"""


def print_reversed_list_integer(my_list=[]):
    my_list.sort(reverse=True)

    if len(my_list) > 1:
        for int in my_list:
            print("{:d}".format(int))
