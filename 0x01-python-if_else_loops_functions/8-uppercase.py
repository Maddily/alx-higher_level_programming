#!/usr/bin/python3
"""Transform a string into uppercase and print it"""


def uppercase(str):
    for char in str:
        print("{}".format(chr(ord(char) - 32) if ord(char) >= 97
                          and ord(char) <= 122 else char), end="")

    print()
