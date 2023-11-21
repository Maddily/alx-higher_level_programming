#!/usr/bin/python3
"""Define a Square type of object"""


class Square:
    """Define a private attribute"""

    def __init__(self, size=0):
        """Initialize <size> private attribute to what would be passed
        as an argument for <size>"""

        self.__size = size

        self.is_int()

    def is_int(self):
        """Check if a value is an integer"""

        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Return the area of the square"""

        return self.__size ** 2

    @property
    def size(self):
        """Retrieve the size"""

        return self.__size

    @size.setter
    def size(self, value):
        """Set the size"""

        self.__size = value

        self.is_int()

    def my_print(self):
        """Print the square"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
