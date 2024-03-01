#!/usr/bin/python3
"""
This script takes someone's GitHub credentials (username and password/token)
and uses the GitHub API to display their id
"""

import requests
from sys import argv


if __name__ == "__main__":
    user_name = argv[1]
    password = argv[2]

    url = "https://api.github.com/user"

    response = requests.get(url, auth=(user_name, password))

    if response.status_code == 200:
        print(response.json().get('id'))
    else:
        print(None)
