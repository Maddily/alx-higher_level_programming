#!/usr/bin/python3

def best_score(a_dictionary):
    """Find the key with the largest integer value"""

    if a_dictionary is None or not a_dictionary:
        return None

    key = max(a_dictionary, key=lambda k: a_dictionary[k])

    return key
