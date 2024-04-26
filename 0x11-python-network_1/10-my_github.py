#!/usr/bin/python3
"""This function does the following:
- it takes my github credentials 
- then it uses the GitHub API to display my github id.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
