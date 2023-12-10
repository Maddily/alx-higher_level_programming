#!/usr/bin/python3
"""
Module Name: rectangle

Description: This module defines a class `Rectangle`
that inherits from Base.
"""
from models.base import Base


class Rectangle(Base):
    """
    Defines a rectangle

    Methods:
    - area()-> int: Returns the area of a rectangle
    - display(): Prints a rectangle
    - __str__()-> str: Returns a string representation for
    a rectangle object
    - update(): Updates attributes
    - to_dictionary()-> dict: Returns the dictionary representation
    of a rectangle object
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        width: A Rectangle object's width
        height: A Rectangle object's height
        x: A Rectangle object's horizontal position
        y: A Rectangle object's vertical position
        id: The identifier for a Rectangle object
        """

        if type(width) != int:
            raise TypeError("width must be an integer")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if type(x) != int:
            raise TypeError("x must be an integer")
        if type(y) != int:
            raise TypeError("y must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")

        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id)

    @property
    def width(self):
        """Retrieves `width`"""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets `width`"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves `height`"""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets `height`"""

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieves x"""

        return self.__x

    @x.setter
    def x(self, value):
        """Sets `x`"""

        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieves `y`"""

        return self.__y

    @y.setter
    def y(self, value):
        """Sets `y`"""

        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of a Rectangle object"""

        return self.__width * self.__height

    def display(self):
        """Prints a rectangle object filled
        with # character"""

        rectangle_line = (' ' * self.__x) + ('#' * self.__width) + '\n'
        rectangle = ('\n' * self.__y) + (rectangle_line * self.__height)

        print(rectangle, end="")

    def __str__(self):
        """Returns a string representation of a rectangle"""

        return (
            f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}/{self.height}"
        )

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
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        super().__init__(arg)
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
                i += 1
        elif kwargs:
            for attr, value in kwargs.items():
                if attr == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        super().__init__(value)
                elif hasattr(self, attr):
                    setattr(self, attr, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a rectangle"""

        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
