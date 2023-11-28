#!/usr/bin/python3
"""
Module Name: 2-matrix_divided

Description:
    This module contains a function that divides
    elements of a given matrix by a given number.

Functions:
    - matrix_divided: Divides elements of a given matrix
    by a given number
"""


def matrix_divided(matrix, div):
    """
    Divides elements of a given matrix by a given number

    Parameters:
    - matrix: The first parameter.
    - div (number): The second parameter.

    Returns:
    A new matrix which is the result of dividing the matrix by div.
    """

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )

    for i in matrix:
        if not isinstance(i, list) or len(i) == 0:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )

        for j in i:
            if (
                    (not isinstance(j, int) and not isinstance(j, float))
                    or isinstance(j, bool)
            ):
                raise TypeError(
                    "matrix must be a matrix"
                    " (list of lists) of integers/floats"
                    )

    size = len(matrix[0])

    for lst in matrix:
        if len(lst) != size:
            raise TypeError("Each row of the matrix must have the same size")

    if (
            (not isinstance(div, int) and not isinstance(div, float))
            or isinstance(div, bool)
    ):
        raise TypeError("div must be a number")

    if div == 0 or div == 0.0 or div == -0 or div == -0.0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(element / div, 2) for element in lst]
                  for lst in matrix]

    return new_matrix
