#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    # calcular len_args
    len_args = len(argv) -1
    if len_args == 0:
    # imprimir "0 arguments."
        print("0 arguments.")
    elif len_args == 1:
    # imprimir "1 argument:"
        print("1 argument:")
    else:
    # imprimir "<len_args> arguments:"
        print(f"{len_args} arguments:")
for i in range(1, len_args + 1):
    # imprimir "<i>: <argv[i]>"
    print(f"{i}: {argv[i]}")
