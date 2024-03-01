#!/usr/bin/python3
"""
This script takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response
"""

from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}

    data = urlencode(email).encode('ascii')

    request = Request(url, data)

    with urlopen(request) as response:
        body = response.read()

    print(body.decode('utf-8'))
