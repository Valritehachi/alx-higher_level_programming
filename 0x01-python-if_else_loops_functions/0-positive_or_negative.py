#!/usr/bin/python3
import random

number = random.randint(-10, 10)

if number > 0:
    message = f"{number} is positive"
elif number == 0:
    message = f"{number} is zero"
else:
    message = f"{number} is negative"

print(message)
