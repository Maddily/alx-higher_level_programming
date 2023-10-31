#!/usr/bin/python3
import random
"""Generate a random number and print its last digit"""

num = random.randint(-10000, 10000)
last_digit = abs(num) % 10
last_digit = -last_digit if num < 0 else last_digit

print(f"Last digit of {num} is {last_digit} and is ", end="")

last_digit = -last_digit if num < 0 else last_digit

if last_digit > 5:
    print("greater than 5")
elif last_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
