#!/usr/bin/python3
"""
Module Name: 7-add_item

Description: This module adds all command line arguments
to a Python list and saves it to a file.
"""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    arguments = sys.argv[1:]

    try:
        existing_data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_data = []

    existing_data.extend(arguments)

    save_to_json_file(existing_data, "add_item.json")
