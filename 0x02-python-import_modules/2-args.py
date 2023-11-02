#!/usr/bin/python3
"""Print the number of arguments this program receives and list them"""


from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(len(argv) - 1))
        for i, arg in enumerate(argv):
            if i != 0:
                print("{}: {}".format(i, arg))
