#!/usr/bin/python3
"""Display a matrix of integers"""


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for int in row:
            print("{}".format(int), end="")
            if row.index(int) != len(row) - 1:
                print(" ", end="")
        print()
