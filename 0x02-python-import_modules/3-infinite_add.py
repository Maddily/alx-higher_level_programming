#!/usr/bin/python3
"""Display the result of the sum of all arguments"""


if __name__ == "__main__":
    from sys import argv
    sum = 0

    for i, arg in enumerate(argv):
        if i != 0:
            sum += int(arg)

    print(sum)
