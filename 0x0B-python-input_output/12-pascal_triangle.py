#!/usr/bin/python3
"""
Module Name: 12-pascal_triangle

Description: This module defines a function `pascal_triangle`.
Check the function's documentation for details.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal's triangle of n
    """

    triangle = [[1]]

    if n <= 0:
        return []

    for i in range(1, n):
        row =\
            [1] +\
            [triangle[i - 1][j - 1] + triangle[i - 1][j] for j in range(1, i)]\
            + [1]
        triangle.append(row)

    return triangle
