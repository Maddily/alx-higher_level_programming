#!/usr/bin/python3
"""Define a Square type of object"""


class Square:
    """Defines a private attribute"""
    def __init__(self, size):
        """Initializes <size> private attribute to what would be passed
        as an argument for <size>"""

        self.__size = size
