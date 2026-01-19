#!/usr/bin/python3
# function that prints a string in uppercase followed by a new line
def uppercase(str):
    result = ""
    for char in str:
        if ord(char) >=97 and ord(char) <= 122:
            result += chr(ord(char) -32)
        else:
            result = result + char
    print("{}".format(result))
