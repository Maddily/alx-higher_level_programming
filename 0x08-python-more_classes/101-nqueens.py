#!/usr/bin/python3
"""
This module contains a function that solves the N queens problem.
"""
import sys


def place_queens(dimension):
    """
    place_queens: Solves the N queens problem which is a challenge
    of placing N non-attacking queens on an N×N chessboard.
    """

    if not isinstance(dimension, int):
        print("N must be a number")
        sys.exit(1)

    if dimension < 4:
        print("N must be at least 4")
        sys.exit(1)

    row_col_rep = [-1] * dimension

    def is_safe(row, column):
        """Checks if it's safe to place the queen
        at a position"""

        for previous_row in range(row):
            previous_column = row_col_rep[previous_row]
            if (
                    previous_column == column
                    or abs(previous_column - column) == abs(previous_row - row)
            ):
                return False
        return True

    def get_possible_solution():
        """Returns a list representing a possible solution"""

        return [[row, row_col_rep[row]] for row in range(dimension)]

    def backtrack(row):
        """Recursively looks for positions to place queens"""

        if row == dimension:
            print(get_possible_solution())
            return

        for column in range(dimension):
            if is_safe(row, column):
                row_col_rep[row] = column
                backtrack(row + 1)
                row_col_rep[row] = -1

    backtrack(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        dimension = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    place_queens(dimension)
