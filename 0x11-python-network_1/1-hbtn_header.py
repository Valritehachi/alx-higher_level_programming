#!/usr/bin/python3
"""This script does the following
- can take in a url and send and a request to it
- prints out the value found in the header.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
