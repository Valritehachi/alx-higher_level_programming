#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    n = len(sys.argv)
    if n != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    if operator == "+":
        print(f"{a} {operator} {b} = {add(a, b)}")
    elif operator == "-":
        print(f"{a} {operator} {b} = {sub(a, b)}")
    elif operator == "*":
        print(f"{a} {operator} {b} = {mul(a, b)}")
    elif operator == "/":
        print(f"{a} {operator} {b} = {div(a, b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
