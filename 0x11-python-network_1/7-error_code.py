#!/usr/bin/python3
"""
This script takes in a URL and displays the body of the response
"""

import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    response = requests.get(url)

    if response.status_code >= 400:
        print('Error code:', response.status_code)
    else:
        print(response.text)
