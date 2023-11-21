#!/usr/bin/python3
"""Define a Square type of object"""


class Square:
    """Defines a private attribute"""

    def __init__(self, size=0):
        """Initializes <size> private attribute to what would be passed
        as an argument for <size>"""

        self.__size = size

        self.is_number()

    def is_number(self):
        """Checks if a value is a number"""

        if not isinstance(self.__size, (int, float)):
            raise TypeError("size must be a number")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the area of the square"""

        return self.__size ** 2

    @property
    def size(self):
        """Retrieve the size"""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size"""

        self.__size = value

        self.is_number()

    def __eq__(self, other):
        """Compare the areas of two squares"""

        return self.area() == other.area()

    def __ne__(self, other):
        """Compare the areas of two squares"""

        return self.area() != other.area()

    def __lt__(self, other):
        """Compare the areas of two squares"""

        return self.area() < other.area()

    def __le__(self, other):
        """Compare the areas of two squares"""

        return self.area() <= other.area()

    def __gt__(self, other):
        """Compare the areas of two squares"""

        return self.area() > other.area()

    def __ge__(self, other):
        """Compare the areas of two squares"""

        return self.area() >= other.area()
