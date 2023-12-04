#!/usr/bin/python3
"""
Module Name: 1-my_list

Description: This module defines a class that inherits from `list`.
"""


class MyList(list):
    """
    MyList: Defines a list

    Public Instance Methods:
    - print_sorted(): Prints the list, sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list, sorted in ascending order.
        """

        new_list = sorted(self)
        print(new_list)
