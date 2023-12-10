#!/usr/bin/python3
"""
Module Name: square

Description: This module defines a class `Square`
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defines a square.

    Methods:
    - __str__()-> str: Returns the string representation
    of a square object.
    - update(): Updates the values of attributes.
    - to_dictionary()-> dict: Returns the dictionary representation
    of a square object
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieves a square's size"""

        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of a square"""

        self.width = value
        self.height = value

    def __str__(self):
        """Returns a string representation of a square"""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute

        Parameters:
        - args: A list of new attribute values
        - kwargs: Pairs of attributes and their respective values
        """

        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        super().__init__(
                            self.size, self.size, self.x, self.y, arg
                            )
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
                i += 1
        elif kwargs:
            for attr, value in kwargs.items():
                if attr == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        super().__init__(
                            self.size, self.size, self.x, self.y, value
                            )
                elif hasattr(self, attr):
                    setattr(self, attr, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a square object"""

        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
