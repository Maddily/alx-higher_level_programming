#!/usr/bin/python3
import random
"""Generate a random number and print its last digit"""

num = random.randint(-10000, 10000)
if num > 0:
    last_digit = num % 10
elif num < 0:
    last_digit = (num * -1) % 10

if last_digit > 5:
    print(f"Last digit of {num} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {num} is {last_digit} and is 0")
elif last_digit < 6 and last_digit != 0:
    print(f"Last digit of {num} is {last_digit} and is less than 6 and not 0")
