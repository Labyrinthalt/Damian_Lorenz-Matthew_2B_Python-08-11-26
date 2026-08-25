import math

def exponent_menu():
    print("EXPONENTIATION AND LOGARITHMS FUNCTIONS")
    print(""" 
    1. Show the value of e
    2. Compute exp(x)
    3. Compute the natural log, log10, and log2 of a value
    4. Compute log(x, base) with a custom base
    5. Compute pow(x, y) - built-in vs math.pow
    6. Back to main menu
    """)

    choice = input("Enter your choice: ").strip()

    if choice == '1':
        print(f"\nmath.e = {math.e}")

    elif choice == '2':
        x = float(input("Enter a value for x: "))
        print(f"\nexp({x}) = e^{x} = {math.exp(x)}")

    elif choice == '3':
        x = float(input("Enter a positive value for x: "))
        try:
            print(f"\nlog({x}) = {math.log(x)}")
            print(f"log10({x}) = {math.log10(x)}")
            print(f"log2({x}) = {math.log2(x)}")
        except ValueError:
            print("Logarithms require x > 0. Please enter a positive value.")

    elif choice == '4':
        X = float(input("Enter x (must be > 0): "))
        b = float(input("Enter base b (must be > 0 and != 1): "))
        try:
            print(f"\nlog({X},base={b}) = {math.log(X, b)}")
        except ValueError:
            print("Invalid input for a logrithm with that base")\

    elif choice == '5':
        x = float(input("Enter a base for x: "))
        y = float(input("Enter a exponent for y: "))
        print(f"\npow({x}, {y}) = {pow(x, y)}")
        print(f"math.pow({x}, {y}) = {math.pow(x, y)}")
        print("(Note: pow() always returns a float.)")

    elif choice == '6':
        return
    else:
        print("\nInvalid choice")

exponent_menu()