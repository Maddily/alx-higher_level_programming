#!/usr/bin/python3
"""Display all integers of a list, sorted in descending order"""


def print_reversed_list_integer(my_list=[]):

    if my_list:
        for int in reversed(my_list):
            print("{:d}".format(int))
