#!/usr/bin/python3
"""Print all possible different combinations of two digits"""

for i in range(10):
    j = i + 1

    if i == 8 and j == 9:
        print("{}{}".format(i, j))
        break

    while j <= 9:
        print("{}{}, ".format(i, j), end="")
        j += 1
