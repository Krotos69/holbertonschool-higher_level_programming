#!/usr/bin/python3
# checks for lowercase cahracters
# Args:
#c (str): character to be checked
#		Returns:
#		bool: True if c is lowercase, False otherwise
def islower(c):
    if ord(c) >= 97 and ord(c) <=122:
        return True
    else:
        return False
