#!/usr/bin/python3
"""
This script lists 10 commits (from the most recent to oldest)
of a repository using GitHub API
"""

import requests
from sys import argv


if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]

    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()[:10]

        for commit in commits:
            sha = commit.get('sha')
            author = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author}")
