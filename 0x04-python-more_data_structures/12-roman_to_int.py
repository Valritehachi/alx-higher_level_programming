#!/usr/bin/python3
def roman_to_int(roman_string):
    digit_value = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
    saves = {}
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    value = 0
    for digit in roman_string:
        if digit == 'I' or digit == 'X' or digit == 'C':
            if digit not in saves:
                saves[digit] = 0
            saves[digit] += digit_values[digit]
        elif digit == 'V'
            if 'I' in saves
                value -= saves['I']
                del saves['I']
            value += digit_value[digit]
        elif d
