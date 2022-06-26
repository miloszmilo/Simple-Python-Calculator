import os


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If windows use cls
        command = 'cls'
    os.system(command)


def add(x, y):
    return (x + y)


def subtract(x, y):
    return (x - y)


def divide(x, y):
    return float(x / y)


def multiply(x, y):
    return float(x * y)


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
                    "What would you like to do?\n1. Add two numbers(+)\n2. Subtract(-)\n3. Divide(/)\n4. Multiply(*)\n5. Exit(x)\n\n")
            except choice == NULL or choice == "\n" or choice == " ":
                print("That's not a valid option.")
                continue

            if (choice != 'x'):
                print(str(x) + " " + choice + " " + str(y) + " = ")
            else:
                break

            if choice == '+':
                print(add(x, y))
            elif choice == '-':
                print(subtract(x, y))
            elif choice == '/':
                print(divide(x, y))
            elif choice == '*':
                print(multiply(x, y))
            elif choice == 'x':
                print(exit())
            else:
                print("Not a valid option.")
                continue

            input()

            clearConsole()
        # match choice:
        #     case '1':
        #         print(add(x, y))
        #     case '2':
        #         print(subtract(x, y))
        #     case '3':
        #         print(divide(x, y))
        #     case '4':
        #         print(multiply(x, y))
        #     case '5':
        #         print(exit())
