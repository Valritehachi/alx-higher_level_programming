#!/usr/bin/python3
"""This function:
- receives a URL and email address and sends a post request to it
- it then displays the body of the response email.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)
