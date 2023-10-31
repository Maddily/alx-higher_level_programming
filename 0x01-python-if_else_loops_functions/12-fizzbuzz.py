#!/usr/bin/python3
"""Implement Fizz Buzz"""


def fizzbuzz():
    for i in range(1, 101):
        if i % 15:
            print("FizzBuzz ", end="")
        elif i % 3:
            print("Fizz ", end="")
        elif i % 5:
            print("Buzz ", end="")
        else:
            print("{} ".format(i), end="")
