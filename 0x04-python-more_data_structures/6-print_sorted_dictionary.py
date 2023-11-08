#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Print a dictionary by ordered keys"""

    new_dict = {key: a_dictionary[key] for key in sorted(a_dictionary)}

    for k, v in new_dict.items():
        print("{}: {}".format(k, v))
