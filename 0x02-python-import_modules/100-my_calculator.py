#!/usr/bin/python3
"""Import functions from a module and handle basic operations"""


if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    operators = ["+", "-", "*", "/"]

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    match argv[2]:
        case "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        case "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        case "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        case "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
