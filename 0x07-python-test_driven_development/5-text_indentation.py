#!/usr/bin/python3
def text_indentation(text):
    if text is None or not isinstance(text, str):
        raise TypeError("text must be a string")
    output = ""
    split_chars = ('.', ':', '?')
    last_char = None

    for c in text:
        if last_char is None and c == " ":
            continue

        output += c
        if c in split_chars:
            output += '\n\n'
            last_char = None
        else:
            last_char = c

    while(len(output) > 0 and output[-1] == ' '):
        output = output[0:-1]
    print(output, end="")
