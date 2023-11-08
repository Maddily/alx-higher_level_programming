#!/usr/bin/python3

def weight_average(my_list=[]):
    """Find the weighted average"""

    if not my_list:
        return 0

    product_sum = sum(score * weight for score, weight in my_list)
    divisor = sum(weight for _, weight in my_list)

    return product_sum / divisor
