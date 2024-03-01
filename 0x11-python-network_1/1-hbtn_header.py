#!/usr/bin/python3
"""
This script takes a URL as an argument and displays
the value of the X-Request-Id variable
found in the header of the response.
"""

from urllib.request import urlopen
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    with urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))
