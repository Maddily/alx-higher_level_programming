#!/usr/bin/python3
""" This script fetches https://alx-intranet.hbtn.io/status """

from urllib.request import urlopen


if __name__ == "__main__":
    with urlopen('https://alx-intranet.hbtn.io/status') as response:
        data = response.read()

        print('Body response:')
        print('    - type:', type(data))
        print('    - content:', data)
        print('    - utf8 content:', data.decode('utf-8'))
