#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list, integers only"""
    i = 0
    printed = 0
    while x > 0:
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            i += 1
            x -= 1
        else:
            x -= 1
            i += 1
            printed += 1

    print()
    return printed
