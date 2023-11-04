#!/usr/bin/python3
"""Display all integers of a list, sorted in descending order"""


def print_reversed_list_integer(my_list=[]):
    my_list.sort(reverse=True)

    if my_list:
        # for int in reversed(my_list):
        for int in my_list:
            print("{:d}".format(int))
