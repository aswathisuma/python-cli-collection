#A menu-driven Python CLI application that generates patterns and performs mathematical calculations using functions, recursion, and lambda expressions.

import os
import subprocess

# Clear Screen
def clear_screen():
    command = 'cls' if os.name == 'nt' else 'clear'
    try:
        subprocess.run(command, shell=True, check=True)
    except Exception:
        print("\n" * 100)

# Choices
def choices():
    print("\n" + "=" * 40)
    print("1. Print Pyramid Star Pattern")
    print("2. Print Inverted Number Pattern")
    print("3. Calculate Sum of First N Natural Numbers (Recursion)")
    print("4. Calculate Power of a Number (Lambda)")
    print("5. Exit")
    print("\n" + "=" * 40)

# Pyramid Star Pattern
def pyramid_pattern(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

#Inverted Number Pattern
def inverted_number_pattern(n):
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print(j, end="")
        print()

#Sum of First N Natural Numbers
def sum_of_natural_numbers(n):
    if n <= 0:
        return 0
    return n + sum_of_natural_numbers(n - 1)

#Power of a Number using Lambda
powerOfNumbers = lambda base, exponent: base ** exponent


while True:
    clear_screen()
    choices()

    choice = int(input("Enter your choice: "))
    if choice not in [1, 2, 3, 4, 5]:
        print("\nInvalid choice. Please enter 1, 2, 3, 4, or 5.")
        input("Press Enter to continue...")
        continue

    if choice == 1:
        n = int(input("Enter the number of rows: "))
        pyramid_pattern(n)
        input("\nPress Enter to continue...")
    elif choice == 2:
        n = int(input("Enter the number of rows: "))
        inverted_number_pattern(n)
        input("\nPress Enter to continue...")
    elif choice == 3:
        n = int(input("Enter the limit: "))
        result = sum_of_natural_numbers(n)
        print(f"Sum = {result}")
        input("\nPress Enter to continue...")
    elif choice == 4:
        base = float(input("Enter the base: "))
        exponent = int(input("Enter the exponent: "))
        print(f"{base}^{exponent} = {powerOfNumbers(base, exponent)}")
        input("\nPress Enter to continue...")
    elif choice == 5:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
        input("Press Enter to continue...")