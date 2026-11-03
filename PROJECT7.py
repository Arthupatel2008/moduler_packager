import datetime
import time
import math
import random
import string
import uuid
import importlib
def create_file(filename):
    with open(filename, 'w') as f:
        pass
    print("File created successfully!")
def write_file(filename, data):
    with open(filename, 'w') as f:
        f.write(data)
    print("Data written successfully!")
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            print("File Content:")
            print(f.read())
    except FileNotFoundError:
        print("File not found!")
def append_file(filename, data):
    with open(filename, 'a') as f:
        f.write("\n" + data)
    print("Data appended successfully!")
def calculate_factorial(n):
    return math.factorial(n)
def compound_interest(p, r, t):
    return p * (math.pow((1 + r / 100), t))
def trig_calculations(angle_deg):
    rad = math.radians(angle_deg)
    return math.sin(rad), math.cos(rad), math.tan(rad)
def circle_area(radius):
    return math.pi * (radius ** 2)
def datetime_menu():
    while True:
        print("===============================")
        print("Datetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            now = datetime.datetime.now()
            print("Current Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))
        elif choice == '2':
            d1 = input("Enter the first date (YYYY-MM-DD): ")
            d2 = input("Enter the second date (YYYY-MM-DD): ")
            dt1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
            dt2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
            diff = abs((dt2 - dt1).days)
            print(f"Difference: {diff} days")
        elif choice == '3':
            fmt = input("Enter custom format (e.g., %d-%m-%Y): ")
            print("Formatted Date:", datetime.datetime.now().strftime(fmt))
        elif choice == '4':
            input("Press Enter to start the stopwatch...")
            start = time.time()
            input("Press Enter to stop the stopwatch...")
            end = time.time()
            print(f"Elapsed Time: {round(end - start, 2)} seconds")
        elif choice == '5':
            sec = int(input("Enter countdown time in seconds: "))
            while sec > 0:
                print(sec, end=" ", flush=True)
                time.sleep(1)
                sec -= 1
            print("\nTime's up!")
        elif choice == '6':
            break
        else:
            print("Invalid choice!")
def math_menu():
    while True:
        print("===============================")
        print("Mathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            n = int(input("Enter a number: "))
            print("Factorial:", calculate_factorial(n))
        elif choice == '2':
            p = float(input("Enter principal amount: "))
            r = float(input("Enter rate of interest (in %): "))
            t = float(input("Enter time (in years): "))
            amt = compound_interest(p, r, t)
            print(f"Compound Interest: {amt:.2f}")
        elif choice == '3':
            deg = float(input("Enter angle in degrees: "))
            s, c, t = trig_calculations(deg)
            print(f"Sin: {s:.2f}, Cos: {c:.2f}, Tan: {t:.2f}")
        elif choice == '4':
            r = float(input("Enter radius of circle: "))
            print(f"Area of Circle: {circle_area(r):.2f}")
        elif choice == '5':
            break
        else:
            print("Invalid choice!")
def random_menu():
    while True:
        print("===============================")
        print("Random Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            low = int(input("Enter lower bound: "))
            high = int(input("Enter upper bound: "))
            print("Random Number:", random.randint(low, high))
        elif choice == '2':
            size = int(input("Enter list size: "))
            r_list = [random.randint(1, 100) for _ in range(size)]
            print("Random List:", r_list)
        elif choice == '3':
            length = int(input("Enter password length: "))
            chars = string.ascii_letters + string.digits + "!@#$%^&*"
            pwd = "".join(random.choice(chars) for _ in range(length))
            print("Generated Password:", pwd)
        elif choice == '4':
            otp = "".join([str(random.randint(0, 9)) for _ in range(6)])
            print("Generated OTP:", otp)
        elif choice == '5':
            break
        else:
            print("Invalid choice!")
def uuid_menu():
    print("===============================")
    print("Generate Unique Identifiers:")
    print("Generated UUID:", uuid.uuid4())
def file_menu():
    while True:
        print("===============================")
        print("File Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            fname = input("Enter file name: ")
            create_file(fname)
        elif choice == '2':
            fname = input("Enter file name: ")
            data = input("Enter data to write: ")
            write_file(fname, data)
        elif choice == '3':
            fname = input("Enter file name: ")
            read_file(fname)
        elif choice == '4':
            fname = input("Enter file name: ")
            data = input("Enter data to append: ")
            append_file(fname, data)
        elif choice == '5':
            break
        else:
            print("Invalid choice!")
def explore_module():
    print("===============================")
    print("Explore Module Attributes:")
    mod_name = input("Enter module name to explore: ")
    try:
        mod = importlib.import_module(mod_name)
        print(f"Available Attributes in {mod_name} module:")
        print(dir(mod))
    except ModuleNotFoundError:
        print("Module not found!")
def main():
    while True:
        print("===============================")
        print("Welcome to Multi-Utility Toolkit")
        print("===============================")
        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        print("===============================")
        choice = input("Enter your choice: ")
        if choice == '1':
            datetime_menu()
        elif choice == '2':
            math_menu()
        elif choice == '3':
            random_menu()
        elif choice == '4':
            uuid_menu()
        elif choice == '5':
            file_menu()
        elif choice == '6':
            explore_module()
        elif choice == '7':
            print("===============================")
            print("Thank you for using the Multi-Utility Toolkit!")
            print("===============================")
            break
        else:
            print("Invalid choice!")
if __name__ == "__main__":
    main()
