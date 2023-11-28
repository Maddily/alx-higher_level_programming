#!/usr/bin/python3
"""
Module Name: 100-matrix_mul

Description:
    This module provides functionality for multiplication of matrices.

Functions:
    - matrix_mul: Multiplies two matrices
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Parameters:
    - m_a (matrix): The first parameter.
    - m_b (matrix): The second parameter.

    Returns:
    The product of the two matrices.

    Raises:
    TypeError: If either m_a or m_b is not a list.
    TypeError: If either m_a or m_b is not a list of lists.
    ValueError: If either m_a or m_b is empty.
    TypeError: If either m_a or m_b contains an element that is neither
                an integer nor a float.
    TypeError: If either m_a or m_b is not a rectangle
                (all rows are of the same size).
    ValueError: If m_a and m_b can't be multiplied.
    """

    product_matrix = []
    row = []
    product = 0
    i = 0
    j = 0

    # If either m_a or m_b is not a list.
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # If either m_a or m_b is not a list of lists.
    for row_a in m_a:
        if not isinstance(row_a, list):
            raise TypeError("m_a must be a list of lists")
    for row_b in m_b:
        if not isinstance(row_b, list):
            raise TypeError("m_b must be a list of lists")

    # If either m_a or m_b is empty.
    if not m_a or not m_a[0]:
        raise ValueError("m_a can't be empty")
    if not m_b or not m_b[0]:
        raise ValueError("m_b can't be empty")

    row_size_a = len(m_a[0])
    row_size_b = len(m_b[0])

    # If either m_a or m_b contains an element that is neither
    # an integer nor a float.
    for row_a in m_a:
        for k in row_a:
            if (
                    (
                        not isinstance(k, int)
                        and not isinstance(k, float)
                    )
                    or isinstance(k, bool)
            ):
                raise TypeError(
                    "m_a should contain only integers or floats"
                    )

    for row_b in m_b:
        for k in row_b:
            if (
                    (
                        not isinstance(k, int)
                        and not isinstance(k, float)
                    )
                    or isinstance(k, bool)
            ):
                raise TypeError(
                    "m_b should contain only integers or floats"
                    )

    # If either m_a or m_b is not a rectangle
    # (all rows are of the same size).
    for row_a in m_a:
        if len(row_a) != row_size_a:
            raise TypeError("each row of m_a must be of the same size")
    for row_b in m_b:
        if len(row_b) != row_size_b:
            raise TypeError("each row of m_b must be of the same size")

    # If m_a and m_b can't be multiplied.
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    for row_a in m_a:
        cols = len(m_b[0])
        while cols > 0:
            for row_b in m_b:
                # If either m_a or m_b contains an element that is neither
                # an integer nor a float.
                if (
                        (
                            not isinstance(row_a[i], int)
                            and not isinstance(row_a[i], float)
                        )
                        or isinstance(row_a[i], bool)
                ):
                    raise TypeError(
                        "m_a should contain only integers or floats"
                        )
                if (
                        (
                            not isinstance(row_b[j], int)
                            and not isinstance(row_b[j], float)
                        )
                        or isinstance(row_b[j], bool)
                ):
                    raise TypeError(
                        "m_b should contain only integers or floats"
                        )
                product += row_a[i] * row_b[j]
                i += 1
            i = 0
            j += 1
            row.append(product)
            product = 0
            cols -= 1
        j = 0
        product_matrix.append(row)
        row = []

    return product_matrix
