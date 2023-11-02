#!/usr/bin/python3
"""Display all the names defined by a module"""


if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4).sort()

    for name in names:
        if name[0] != "_" and name[1] != "_":
            print("{}".format(name))
