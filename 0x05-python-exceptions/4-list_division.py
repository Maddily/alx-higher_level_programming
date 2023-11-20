#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divide two lists"""
    quotient_list = []
    i = 0

    while list_length > 0:
        try:
            quotient_list.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
            quotient_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            quotient_list.append(0)
        except IndexError:
            print("out of range")
            quotient_list.append(0)
            break
        finally:
            i += 1
            list_length -= 1

    return quotient_list
