#!/usr/bin/python3
"""Display the last digit of a given number"""


def print_last_digit(number):
    last_digit = number % 10 if number >= 0 else -number % 10

    print("{}".format(last_digit), end="")

    return last_digit
