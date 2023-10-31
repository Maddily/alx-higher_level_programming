#!/usr/bin/python3
"""Display the alphabet in reverse, alternating between lower and uppercase"""


i = 122
while i >= 65:
    print("{}".format(chr(i)), end="")
    if i == 65:
        break
    if i >= 97 and i <= 122:
        i -= 33
    else:
        i += 31
