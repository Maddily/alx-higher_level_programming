#!/usr/bin/python3
"""
This module contains a class `LockedClass`
"""


class LockedClass:
    """
    LockedClass: Prevents the use from dynamically
    creating new instance attributes,
    except if the new instance attribute is called first_name.
    """

    def __setattr__(self, name, value):
        """
        Overrides the __setattr__ method

        Parameters:
        - name: The name of an attribute
        - value: The value of the attribute with the name `name`
        """

        if name != "first_name":
            raise AttributeError(
                    f"'LockedClass' object has no attribute '{name}'"
                )
        super().__setattr__(name, value)
