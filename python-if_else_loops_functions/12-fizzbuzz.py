#!/usr/bin/python3
def fizzbuzz():
    # Imprime los números del 1 al 100
    for number in range(1, 101):
        # Comprueba si el número es divisible por 3 y 5
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end=" ")
        # Comprueba si el número es divisible por 3
        elif number % 3 == 0:
            print("Fizz", end=" ")
        # Comprueba si el número es divisible por 5
        elif number % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(number, end=" ")
