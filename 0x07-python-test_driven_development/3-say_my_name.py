#!/usr/bin/python3
"""
Module Name: 3-say_my_name

Description:
    This module contains a function that
    prints My name is <first name> <last name>,
    where <first name> is the first argument,
    and <last name> is the second argument

Functions:
    - say_my_name: Prints a sentense. Check the function
    documentation for more information.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>,
    where <first name> is the first argument,
    and <last name> is the second argument

    Parameters:
    - first_name: The first parameter.
    - last_name: The second parameter.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
