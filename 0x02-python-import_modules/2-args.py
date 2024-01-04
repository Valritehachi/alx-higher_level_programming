#!/usr/bin/python3
import sys

if __name__ == "__main__":
    i = 1
    n = len(sys.argv)
    if n == 1:
        print("0 arguments.")
    elif n == 2:
        print("1 argument:")
    else:
        print(f"{n - 1} arguments:")

    while i < n:
        print(f"{i}: {sys.argv[i]}")
        i = i + 1
