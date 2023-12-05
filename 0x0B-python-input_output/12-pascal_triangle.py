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

    triangle = [[1], [1, 1]]
    sub_triangle = []
    i = 2
    j = 0

    if n <= 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return triangle

    while i < 5:
        while j < i:
            if j == 0:
                sub_triangle.append(1)
                j += 1
            else:
                sub_triangle.append(triangle[i - 1][j - 1]
                                    + triangle[i - 1][j])
                j += 1
        sub_triangle.append(1)
        j = 0
        triangle.append(sub_triangle)
        sub_triangle = []
        i += 1

    return triangle
