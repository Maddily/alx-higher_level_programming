#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """Delete keys with a specific value"""

    keys_to_remove = [k for k, v in a_dictionary.items() if v == value]
    for key in keys_to_remove:
        del a_dictionary[key]
    return a_dictionary
