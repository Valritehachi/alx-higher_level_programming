#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    methods = dir(hidden_4)
    n = len(methods)
    i = 0
    while i < n:
        method = methods[i]
        if method[0:2] != "__":
            print(methods[i])
        i = i + 1
