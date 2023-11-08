#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replace all occurrences of an element by another"""

    # return list(map(lambda x: replace if x == search else x, my_list))

    return [replace if x == search else x for x in my_list]
