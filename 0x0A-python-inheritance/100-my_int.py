#!/usr/bin/python3
"""
Module Name: 100-my_int

Description: This module defines a class `MyInt`.
"""


class MyInt(int):
    """Defines an integer object"""

    def __init__(self, value):
        """Initializes"""

        self.__value = value

    def __eq__(self, value):
        """Returns eq() reversed"""

        return not super().__eq__(value)

    def __ne__(self, value):
        """Returns ne() reversed"""

        return not super().__ne__(value)
