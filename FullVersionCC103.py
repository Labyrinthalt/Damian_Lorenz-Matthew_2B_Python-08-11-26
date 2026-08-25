import sys
import math
import random
import functools

# HELPER FUNCTIONS
def get_float(prompt):
    while True:
        try:
            print(prompt, end="", flush=True)
            sys.stdout.flush()
            return float(input())
        except ValueError:
            print(" >> Invalid input. Please type a number (e.g. 3, 3.5, -2). ")
        except EOFError:
            print("\n >> No input received. Exiting program.")
            raise SystemExit

def get_int(prompt):
    while True:
        try:
            print(prompt, end="", flush=True)
            sys.stdout.flush()
            return int(input())
        except ValueError:
            print(" >> Invalid input. Please type the whole number (e.g., 5, -3, 0).")
        except EOFError:
            print("\n >> No input received. Exiting Program.")
            raise SystemExit

def safe_input(prompt):
    try:
        print(prompt, end="", flush=True)
        sys.stdout.flush()
        return input()
    except EOFError:
        print("\n >> No input received. Exiting Program.")
        raise SystemExit

def pause():
    """Pauses so the user can read the result before the menu reappears."""
    safe_input("\nPress ENTER to return to the menu...")

def print_header(title):
    print("\n" + "=" * 70)
    print(f"{title}")
    print("=" * 70)

# SECTION 1: TRIGONOMETRIC FUNCTIONS
def trig_menu():
    print_header("TRIGONOMETRIC (CIRCULAR) FUNCTIONS")
    print("""
1. Show the value of pi
2. Convert degrees -> radians
3. Convert radians -> degrees
4. Compute sin, cos, tan of an angle
5. Compute asin, acos, atan, of a value (-1 to 1) for asin/ acos
0. Back to main menu""")

    choice = safe_input("Enter your choice: ").strip()
    if choice == "1":
        print(f"math.pi = {math.pi}")

    elif choice == "2":
        deg = get_float("Enter an angle in degrees: ")
        rad = math.radians(deg)
        print(f"\nmath.radians({deg})")
        print(f"\n{deg} degrees = {rad} radians")

    elif choice == "3":
        deg = get_float("Enter an angle in radians: ")
        rad = math.degrees(deg)
        print(f"\nmath.degrees({rad})")
        print(f"\n{rad} radian = {deg} degrees")

    elif choice == "4":
        deg = get_float("Enter an angle in degrees: ")
        rad = math.radians(deg)
        print(f"\nAngle = {deg} degrees ({rad} radians)")
        print(f"sin({deg}) = {math.sin(rad)}")
        print(f"cos({deg}) = {math.cos(rad)}")
        print(f"tan({deg}) = {math.tan(rad)}")

    elif choice == "0":
        return

    else:
        print("\nInvalid choice.")

    pause()

# SECTION 2: HYPERBOLIC FUNCTIONS
def hyperbolic_menu():
    print_header("HYPERBOLIC FUNCTIONS")
    print("""
1. Compute sinh, cosh, tanh of a value x
2. Compute asinh, acosh, atanh of a value x
0. Back to main menu""")

    choice = safe_input("Enter your choice: ").strip()

    if choice == "1":
        x = get_float("Enter a value for x: ")
        print(f"\nFor x = {x}:")
        print(f"sinh({x}) = {math.sinh(x)}")
        print(f"cosh({x}) = {math.cosh(x)}")
        print(f"tanh({x}) = {math.tanh(x)}")

    elif choice == "2":
        x = get_float("Enter a value for x: ")
        print(f"\nFor x = {x}:")
        print(f"asinh({x}) = {math.asinh(x)}")
        
        try:
            print(f"acosh({x}) = {math.acosh(x)}")
        except ValueError:
            print(f"acosh({x}) needs x >= 1. Skipped.")

        try:
            print(f"atanh({x}) = {math.atanh(x)}")
        except ValueError:
            print(f"atanh({x}) needs -1 < x < 1. Skipped.")

    elif choice == "0":
        return

    else:
        print("\nInvalid choice.")

    pause()

# SECTION 3: EXPONENTIATION AND LOGARITHMIC FUNCTIONS
def exponent_menu():
    print_header("EXPONENTIATION AND LOGARITHMIC FUNCTIONS")
    print("""
1. Show the value of e
2. Compute exp(x)
3. Compute the natural log, log10, and log2 of a value
4. Compute log(x, base) with a custom base
5. Compute pow(x, y) - built-in vs math.pow
0. Back to main menu""")

    choice = safe_input("Enter your choice: ").strip()

    if choice == '1':
        print(f"\nmath.e = {math.e}")

    elif choice == '2':
        x = get_float("Enter a value for x: ")
        print(f"\nexp({x}) = e^{x} = {math.exp(x)}")

    elif choice == '3':
        x = get_float("Enter a positive value for x: ")
        try:
            print(f"\nlog({x}) = {math.log(x)}")
            print(f"log10({x}) = {math.log10(x)}")
            print(f"log2({x}) = {math.log2(x)}")
        except ValueError:
            print("Logarithms require x > 0. Please enter a positive value.")

    elif choice == '4':
        X = get_float("Enter x (must be > 0): ")
        b = get_float("Enter base b (must be > 0 and != 1): ")
        try:
            print(f"\nlog({X}, base={b}) = {math.log(X, b)}")
        except ValueError:
            print("Invalid input for a logarithm with that base.")

    elif choice == '5':
        x = get_float("Enter a base for x: ")
        y = get_float("Enter an exponent for y: ")
        print(f"\npow({x}, {y}) = {pow(x, y)}")
        print(f"math.pow({x}, {y}) = {math.pow(x, y)}")
        print("(Note: math.pow() always returns a float.)")

    elif choice == '0':
        return

    else:
        print("\nInvalid choice.")

    pause()

# SECTION 4: GENERAL-PURPOSE MATH FUNCTIONS
def general_menu():
    print_header("GENERAL-PURPOSE MATH FUNCTIONS")
    print("""
1. Compute ceil, floor, and trunc of a value
2. Compute a factorial
3. Compute the hypotenuse of a right triangle
0. Back to Main Menu""")

    choice = safe_input("Enter your choice: ").strip()

    if choice == '1':
        x = get_float("Enter a value for x: ")
        print(f"\nmath.ceil({x}) = {math.ceil(x)}")
        print(f"math.floor({x}) = {math.floor(x)}")
        print(f"math.trunc({x}) = {math.trunc(x)}")

    elif choice == '2':
        x = get_int("Enter a non-negative integer for x: ")
        try:
            print(f"\nmath.factorial({x}) = {math.factorial(x)}")
        except ValueError:
            print("Factorial requires a non-negative integer.")

    elif choice == '3':
        a = get_float("Enter the length of side a: ")
        b = get_float("Enter the length of side b: ")
        print(f"\nmath.hypot({a}, {b}) = {math.hypot(a, b)}")

    elif choice == '0':
        return

    else:
        print("\nInvalid choice.")

    pause()

# SECTION 5: RANDOM MODULE
def random_menu():
    print_header("THE RANDOM MODULE")
    print("""
1. Set a seed (so results can be repeated)
2. Generate a number with randrange()
3. Generate a number with randint()
4. Pick a random item from a list with choice()
5. Draw several UNIQUE items from a list with sample() (like a lottery)
0. Back to Main Menu""")

    choice = safe_input("Enter your choice: ").strip()

    if choice == '1':
        s = get_int("Enter an integer seed value: ")
        random.seed(s)
        print(f"\nRandom seed set to {s}.")

    elif choice == '2':
        start = get_int("Enter start value: ")
        stop = get_int("Enter stop value: ")
        step = get_int("Enter step value: ")
        try:
            result = random.randrange(start, stop, step)
            print(f"\nrandom.randrange({start}, {stop}, {step}) = {result}")
        except ValueError:
            print("Invalid step or range bounds for randrange().")

    elif choice == '3':
        a = get_int("Enter minimum value (inclusive): ")
        b = get_int("Enter maximum value (inclusive): ")
        try:
            result = random.randint(a, b)
            print(f"\nrandom.randint({a}, {b}) = {result}")
        except ValueError:
            print("Minimum value cannot be greater than maximum value.")

    elif choice == '4':
        items_input = safe_input("Enter items separated by spaces: ").strip().split()
        if items_input:
            selected = random.choice(items_input)
            print(f"\nrandom.choice({items_input}) = '{selected}'")
        else:
            print("List cannot be empty.")

    elif choice == '5':
        items_input = safe_input("Enter items separated by spaces: ").strip().split()
        if not items_input:
            print("List cannot be empty.")
        else:
            k = get_int("Enter number of unique items to pick: ")
            try:
                sample_result = random.sample(items_input, k)
                print(f"\nrandom.sample({items_input}, {k}) = {sample_result}")
            except ValueError:
                print("Sample size cannot be larger than the population size or negative.")

    elif choice == '0':
        return

    else:
        print("\nInvalid choice.")

    pause()

# MAIN MENU CONTROLLER
def main():
    print("=" * 70)
    print("WELCOME TO THE MATH & RANDOM MODULE MINI SYSTEM")
    print("A learning tool for Python's 'math' and 'random' module")
    print("=" * 70)

    while True:
        print("""
MAIN MENU
    1. Trigonometric (circular) functions - sin, cos, tan, pi, radians...
    2. Hyperbolic functions - sinh, cosh, tanh, asinh...
    3. Exponential & logarithmic functions - e, exp, log, log10, log2...
    4. General-purpose math functions - ceil, floor, trunc, factorial...
    5. Random module - seed, randrange, randint, choice, sample
    0. Exit the program
""")

        choice = safe_input("Enter your choice (0-5): ").strip()

        if choice == "1":
            trig_menu()
        elif choice == "2":
            hyperbolic_menu()
        elif choice == "3":
            exponent_menu()
        elif choice == "4":
            general_menu()
        elif choice == "5":
            random_menu()
        elif choice == "0":
            print("\nThank you for exploring the math and random modules. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number from 0-5. ")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Goodbye!")
    except SystemExit:
        pass