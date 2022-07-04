import os
import math


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If windows use cls
        command = 'cls'
    os.system(command)


def addition(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return float(x * y)


def divide(x, y):
    return float(x / y)


def power(x, y):
    return math.pow(x, y)


def root(x, y):
    if y == 2:
        return math.sqrt(x)  # or return x**(1/2)
    return math.pow(x, (1/y))  # or return x**(1/y)


def sinus(x):
    return math.sin(x)


def cosinus(x):
    return math.sin(x)


def tangent(x):
    return math.tan(x)


def switch(option, x, y):

    if option == '+':
        return (addition(x, y))
    elif option == '-':
        return (subtract(x, y))
    elif option == '*':
        return (multiply(x, y))
    elif option == '/':
        return (divide(x, y))
    elif option == "pow":
        return (power(x, y))
    elif option == "root":
        return (root(x, y))
    elif option == 'sin':
        return (sinus(x))
    elif option == 'cos':
        return (cosinus(x))
    elif option == 'tan':
        return (tangent(x))
    return ("That's not a valid option")


if __name__ == "__main__":
    while True:
        x = input(
            "Welcome to Python Calculator 1.0\n\nPlease provide two numbers that you want to operate on\t")
        y = input("Now the second number\t")
        print("Are these numbers okay?(y/n)" + x + " " + y)

        if (input().lower() == "n"):
            continue

        x = float(x)
        y = float(y)

        while True:
            try:
                choice = str.lower(input(
                    "What would you like to do?\nAddition(+)\nSubtract(-)\nMultiply(*)\nDivide(/)\nPower(pow)\nRoot(root)\nSinus(sin)\nCosinus(cos)\nTangent(tan)\nPick new numbers(p)\nExit(x)\n\n"))
            except choice == NULL or choice == "\n" or choice == " ":
                print("That's not a valid option.")
                continue

            if (choice == 'x'):
                exit

            if (choice == 'p'):
                clearConsole()
                break
            if (choice != "sin" or choice != "tan"):
                print(str(x) + " " + choice + " " + str(y) + " = ")
            print(str(x) + " " + choice + " = ")

            print(switch(choice, x, y))

            input()

            clearConsole()
