import math

def general_math_menu():
    print("GENERAL-PURPOSE MATH FUNCTIONS")
    print(""" 
    1. Compute ceil, floor, and trunc of a value
    2. Compute a factorial
    3. Compute the hypotenuse of a right triangle
    0. Back to Main Menu
    """)

    choice = input("Enter your choice: ").strip()

    if choice == '1':
        x = float(input("Enter a value for x: "))
        print(f"\nmath.ceil({x}) = {math.ceil(x)}")
        print(f"math.floor({x}) = {math.floor(x)}")
        print(f"math.trunc({x}) = {math.trunc(x)}")

    elif choice == '2':
        x = int(input("Enter a non-negative integer for x: "))
        try:
            print(f"\nmath.factorial({x}) = {math.factorial(x)}")
        except ValueError:
            print("Factorial requires a non-negative integer.")

    elif choice == '3':
        a = float(input("Enter the length of side a: "))
        b = float(input("Enter the length of side b: "))
        print(f"\nmath.hypot({a}, {b}) = {math.hypot(a, b)}")

    elif choice == '0':
        return

    else:
        print("\nInvalid choice")

general_math_menu()