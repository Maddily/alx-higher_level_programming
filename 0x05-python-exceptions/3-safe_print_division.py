#!/usr/bin/python3
def safe_print_division(a, b):
    """Divide two integers and print the result"""
    quotient = None

    try:
        quotient = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(quotient))

    return quotient
