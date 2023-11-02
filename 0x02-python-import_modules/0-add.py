#!/usr/bin/python3
from add_0 import add

"""Import a function from a module and call it"""


a = 1
b = 2

if __name__ == "__main__":
    import sys
    print("{} + {} = {}".format(a, b, add(a, b)))
