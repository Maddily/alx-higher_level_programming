#!/usr/bin/python3
"""Define a Square type of object"""


class Square:
    """Defines a private attribute"""

    def __init__(self, size=0):
        """Initializes <size> private attribute to what would be passed
        as an argument for <size>"""

        self.__size = size

        self.is_int()

    def is_int(self):
        """Checks if a value is an integer"""

        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the area of the square"""

        self.is_int()

        return self.__size ** 2

    @property
    def size(self):
        """Retrieve the size"""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size"""

        self.__size = value
