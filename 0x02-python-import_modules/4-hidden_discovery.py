#!/usr/bin/python3
"""Display all the names defined by a module"""


if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    names.sort()

    for name in names:
        if not name.startswith("__"):
            print(name)
