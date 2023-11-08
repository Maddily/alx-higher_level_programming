#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """Replace/add a key:value pair in a dictionary"""

    new_dict = a_dictionary.copy()
    new_dict[key] = value

    return new_dict
