#!/usr/bin/python3

def roman_to_int(roman_string):
    """Convert a roman numeral to an integer"""

    if type(roman_string) is not str or roman_string is None:
        return 0

    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                      'C': 100, 'D': 500, 'M': 1000}
    integer = 0
    previous_value = 0

    for numeral in roman_string:
        value = roman_numerals.get(numeral, 0)

        if value > previous_value:
            integer += value - (2 * previous_value)
        else:
            integer += value

        previous_value = value

    return integer
