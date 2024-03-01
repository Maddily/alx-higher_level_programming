#!/usr/bin/python3
"""
This script takes in a URL and displays the body of the response
"""

from urllib.request import urlopen, Request
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    try:
        with urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code:', e.code)
