#!/usr/bin/python3
"""Define a Square type of object"""


class Square:
    """Defines a private attribute"""

    def __init__(self, size=0):
        """Initializes <size> private attribute to what would be passed
        as an argument for <size>"""

        self.__size = size

        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the area of the square"""

        return self.__size ** 2
