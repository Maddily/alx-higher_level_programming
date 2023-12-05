#!/usr/bin/python3
"""
Module Name: 10-student

Description: This module defines a class `Student`.
Check the class's documentation for details.
"""


class Student:
    """
    Defines a student

    Attributes:
    - first_name: A student's first name
    - last_name: A student's last name
    - age: A student's age

    Methods:
    - to_json() -> dict: Retrieves a dictionary representation of
    a Student instance
    """

    def __init__(self, first_name, last_name, age):
        """Initializes"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
         Retrieves a dictionary representation of
         a Student instance

         Parameters:
         - attrs: Could be a list of attribute names
        """

        if attrs:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)
                    and not callable(getattr(self, attr))}

        return {attr: getattr(self, attr) for attr in self.__dict__
                if not callable(getattr(self, attr))}
