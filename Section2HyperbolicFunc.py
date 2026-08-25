import math

# SECTION 2: HYPERBOLIC FUNCTIONS

def hyperbolic_functions():
        print("HYPERBOLIC FUNCTION")
        print("""
 1. Compute sinh, cosh, tanh of a value x
 2. Compute asinh, acosh, atanh of a value x
 0. Exit
        """)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            try:
                x = float(input("Enter a value for x: "))
                print(f"\nFor x = {x}:")
                print(f"sinh({x}) = {math.sinh(x)}")
                print(f"cosh({x}) = {math.cosh(x)}")
                print(f"tanh({x}) = {math.tanh(x)}")
            except ValueError:
                print("Invalid number! Please enter a valid number.")

        elif choice == "2":
            try:
                x = float(input("Enter a value for x: "))
                print(f"asinh({x}) = {math.asinh(x)}")
                
                try:
                    print(f"acosh({x}) = {math.acosh(x)}")
                except ValueError:
                    print(f"acosh({x}) needs x >= 1. Skipped.")

                try:
                    print(f"atanh({x}) = {math.atanh(x)}")
                except ValueError:
                    print(f"atanh({x}) needs -1 < x < 1. Skipped.")

            except ValueError:
                print("Invalid number! Please enter a valid number.")

        elif choice == "0":
            print("Exit successful.")
            return

        else:
            print("Invalid choice.")
print(hyperbolic_functions())