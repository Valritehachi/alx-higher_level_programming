#!/usr/bin/python3
"""This script does the following
- receives a url and sends a request to it
- then it displays the body of the response received.
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
