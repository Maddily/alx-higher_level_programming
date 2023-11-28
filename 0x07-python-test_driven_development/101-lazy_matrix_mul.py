#!/usr/bin/python3
"""
Module Name: 101-lazy_matrix_mul

Description:
    This module provides functionality for multiplication of matrices.

Functions:
    - lazy_matrix_mul: Multiplies two matrices
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Parameters:
    - m_a (matrix): The first parameter.
    - m_b (matrix): The second parameter.

    Returns:
    The product of the two matrices.
    """

    return numpy.matmul(m_a, m_b)
