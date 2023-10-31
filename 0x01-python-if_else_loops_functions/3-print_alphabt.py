#!/usr/bin/python3
char = 97

while char < 123:
    if char != 113 and char != 101:
        print("{}".format(chr(char)), end="")
    char += 1
