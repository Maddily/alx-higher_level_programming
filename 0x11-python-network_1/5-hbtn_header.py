#!/usr/bin/python3
"""
This script takes a URL as an argument and displays
the value of the X-Request-Id variable
found in the header of the response.
"""

import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    response = requests.get(url)
    print(response.headers['X-Request-Id'])
