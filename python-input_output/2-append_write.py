#!/usr/bin/python3

def append_write(filename="", text=""):
    """Append a string to text file and return the """
    with open(filename, "a", encoding="utf-8") as file: # Open the file in append mode with UTF-8 encoding
        return file.write(text) # Append the text to the file and return the number of characters written
