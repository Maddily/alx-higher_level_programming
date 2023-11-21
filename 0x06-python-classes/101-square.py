#!/usr/bin/python3
"""Define a Square type of object"""


class Square:
    """Define a private attribute"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize <size> private attribute to what would be passed
        as an argument for <size>"""

        self.__size = size
        self.__position = position

        self.is_int()
        self.check_position()

    def is_int(self):
        """Check if a value is an integer"""

        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def check_position(self):
        """Check if the position is valid"""

        if (
                not isinstance(self.__position, tuple)
                or len(self.__position) != 2
                or not isinstance(self.__position[0], int)
                or not isinstance(self.__position[1], int)
                or self.__position[0] < 0
                or self.__position[1] < 0
                ):
            raise TypeError("position must be a tuple of 2 positive integers")

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

    @property
    def position(self):
        """Retrieve the position"""

        return self.__position

    @position.setter
    def position(self, value):
        """Set the position"""

        self.__position = value
        self.check_position()

    def my_print(self):
        """Print the square"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for m in range(self.__size):
                    print("#", end="")
                print()

    def __str__(self):
        """Return a string representation of the square"""

        if self.__size != 0:
            for i in range(self.__position[1]):
                print()
        for j in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for m in range(self.__size):
                print("#", end="")
            if j != self.__size - 1:
                print()
        return ""
