#!/bin/bash
# Sends a request to a URL and displays the status code of the response
curl -sI -o /dev/null -w '%{http_code}' "$1"
