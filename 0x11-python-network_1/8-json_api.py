#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import requests
from sys import argv


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'

    if len(argv) == 1:
        q = ""
    else:
        q = argv[1]

    response = requests.post(url, data={'q': q})

    try:
        dict = response.json()

        if dict:
            print(f"[{dict.get('id')}] {dict.get('name')}")
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
