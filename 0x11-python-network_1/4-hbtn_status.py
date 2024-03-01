#!/usr/bin/python3
"""
This script fetches a url
"""

import requests


if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('    - type:', type(response.text))
    print('    - content:', response.text)
