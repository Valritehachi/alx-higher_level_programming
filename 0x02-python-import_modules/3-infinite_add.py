#!/usr/bin/python3
import sys

if __name__ == "__main__":
    i = 1
    n = len(sys.argv)
    if n == 1:
        print("0")
    else:
        total = 0
        while i < n:
            total = total + int(sys.argv[i])
            i = i + 1
        print(total)
