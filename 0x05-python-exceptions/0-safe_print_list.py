#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list"""
    i = 0
    while x > 0:
        try:
            print(my_list[i], end="")
        except Exception:
            break
        else:
            i += 1
            x -= 1
    print()
    return i
