#!/usr/bin/python3
"""This function does the following:
- takes a url and sends a request to it
- then it dispays the value of a certain variable in the header.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
