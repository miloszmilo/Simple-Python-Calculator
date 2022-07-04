import os
import math


OPTIONS = {add(x, y), subtract(x, y), multiply(x, y), divide(x, y), power(
    x, y), root(x, y), sinus(x, y), cosinus(x, y), tangent(x, y)}


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If windows use cls
        command = 'cls'
    os.system(command)


def add(x, y):
    return (x + y)


def subtract(x, y):
    return (x - y)


def multiply(x, y):
    return float(x * y)


def divide(x, y):
    return float(x / y)


def power(x, y):
    return math.pow(x, y)


def root(x, y):
    if y is 2:
        return math.sqrt(x)  # or return x**(1/2)
    return math.pow(x, (1/y))  # or return x**(1/y)


def sinus(x):
    return math.sin(x)


def cosinus(x):
    return math.sin(x)


def tangent(x):
    return math.tan(x)


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
                choice = input(
                    "What would you like to do?\nAdd two numbers(1)\nSubtract(2)\nMultiply(3)\nDivide(4)\nPower(5)\nRoot(6)\nSin(7)\nCos(8)\nTan(9)\nExit(x)\n\n")
            except choice == NULL or choice == "\n" or choice == " ":
                print("That's not a valid option.")
                continue

            if (choice != 'x'):
                print(str(x) + " " + choice + " " + str(y) + " = ")
            else:
                break

            if choice == 'x':
                exit

            print(OPTIONS[choice])

            input()

            clearConsole()
