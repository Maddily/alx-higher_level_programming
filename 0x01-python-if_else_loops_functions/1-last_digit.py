#!/usr/bin/python3
import random
"""Generate a random number and print its last digit"""

num = random.randint(-10000, 10000)
last_digit = abs(num) % 10
last_digit = -last_digit if num < 0 else last_digit

print(f"Last digit of {num:d} is {last_digit:d} and is ", end="")

if last_digit > 5:
    print("greater than 5")
elif last_digit < 6 and last_digit != 0:
    print("less than 6 and not 0")
else:
    print("0")
