#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Execute a function safely"""

    try:
        result = fct(*args)
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return None
    else:
        return result
