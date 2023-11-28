#!/usr/bin/python3
"""
Module Name: 5-text_indentation

Description:
    This module contains a function that prints a text
    with 2 new lines after each `.`, `?` and `:`.

Functions:
    - text_indentation: Prints a text with 2 new lines
    after each `.`, `?` and `:`.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines
    after each `.`, `?` and `:`.

    Parameters:
    - text: The text to be processed.
    """

    chars = ".?:"
    new_line = "\n"
    lines = []
    current_line = ""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in text:
        current_line += char

        if char in new_line:
            lines.append(current_line)
            current_line = ""
        elif char in chars:
            lines.append(current_line.strip())
            current_line = ""

    lines.append(current_line.strip())

    for line in lines:
        if line and line[-1] in new_line:
            print(line, end="")
        elif line:
            print(line)
            if line[-1] in chars:
                print()
