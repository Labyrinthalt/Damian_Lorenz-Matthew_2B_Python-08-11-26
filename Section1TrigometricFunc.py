import math

# SECTION 1: TRIGONOMETRIC (CIRCULAR) FUNCTIONS
def trig_menu():
    print("TRIGONOMETRIC (CIRCULAR) FUNCTIONS")
    print("""
    1. Show the value of pi
    2. Convert degrees -> radians
    3. Convert radians -> degrees
    4. Compute sin, cos, tan of an angle
    5. Compute asin, acos, atan of a value (-1 to 1 for asin/acos)
    0. Back to Main Menu
    """)

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        print(f"\nmath.pi = {math.pi}")

    elif choice == "2":
        deg = float(input("Enter an angle in degrees: "))
        rad = math.radians(deg)
        print(f"\nmath.radians({deg})")
        print(f"{deg} degrees = {rad} radians")

    elif choice == "3":
        rad_val = float(input("Enter an angle in radians: "))
        deg = math.degrees(rad_val)
        print(f"\nmath.degrees({rad_val})")
        print(f"{rad_val} radians = {deg} degrees")

    elif choice == "4":
        deg = float(input("Enter an angle in degrees: "))
        rad = math.radians(deg)
        print(f"\nAngle = {deg} degrees ({rad} radians)")
        print(f"sin({deg}) = {math.sin(rad)}")
        print(f"cos({deg}) = {math.cos(rad)}")
        print(f"tan({deg}) = {math.tan(rad)}")

    elif choice == "5":
        val = float(input("Enter a value between -1 and 1: "))
        try:
            print(f"\nasin({val}) = {math.asin(val)}")
            print(f"acos({val}) = {math.acos(val)}")
        except ValueError:
            print("\nasin and acos require a value between -1 and 1.")
        print(f"atan({val}) = {math.atan(val)}")

    elif choice == "0":
        return

    else:
        print("\nInvalid choice.")

trig_menu()