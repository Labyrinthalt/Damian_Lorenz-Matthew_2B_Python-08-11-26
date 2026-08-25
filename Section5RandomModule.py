import random

def random_module_menu():
    print("THE RANDOM MODULE")
    print(""" 
    1. Set a seed (so results can be repeated)
    2. Generate a number with randrange()
    3. Generate a number with randint()
    4. Pick a random item from a list with choice()
    5. Draw several UNIQUE items from a list with sample() (like a lottery)
    0. Back to Main Menu
    """)

    choice = input("Enter your choice: ").strip()

    if choice == '1':
        s = int(input("Enter an integer seed value: "))
        random.seed(s)
        print(f"\nRandom seed set to {s}.")

    elif choice == '2':
        start = int(input("Enter start value: "))
        stop = int(input("Enter stop value: "))
        step = int(input("Enter step value: "))
        try:
            result = random.randrange(start, stop, step)
            print(f"\nrandom.randrange({start}, {stop}, {step}) = {result}")
        except ValueError:
            print("Invalid range or step values.")

    elif choice == '3':
        a = int(input("Enter minimum value (inclusive): "))
        b = int(input("Enter maximum value (inclusive): "))
        try:
            result = random.randint(a, b)
            print(f"\nrandom.randint({a}, {b}) = {result}")
        except ValueError:
            print("Minimum value cannot be greater than maximum value.")

    elif choice == '4':
        items_input = input("Enter items separated by spaces: ").strip().split()
        if items_input:
            selected = random.choice(items_input)
            print(f"\nrandom.choice({items_input}) = '{selected}'")
        else:
            print("List cannot be empty.")

    elif choice == '5':
        items_input = input("Enter items separated by spaces: ").strip().split()
        if not items_input:
            print("List cannot be empty.")
        else:
            k = int(input("Enter number of unique items to pick: "))
            try:
                sample_result = random.sample(items_input, k)
                print(f"\nrandom.sample({items_input}, {k}) = {sample_result}")
            except ValueError:
                print("Sample size cannot be larger than the population size or negative.")

    elif choice == '0':
        return

    else:
        print("\nInvalid choice")

random_module_menu()