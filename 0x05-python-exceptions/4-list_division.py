#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divide two lists"""
    quotient_list = []
    i = 0

    while list_length > 0:
        try:
            if i < len(my_list_1) and i < len(my_list_2):
                quotient_list.append(my_list_1[i] / my_list_2[i])
            else:
                print("out of range")
                quotient_list.append(0)
        except TypeError:
            print("wrong type")
            quotient_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            quotient_list.append(0)
        finally:
            i += 1
            list_length -= 1

    return quotient_list
