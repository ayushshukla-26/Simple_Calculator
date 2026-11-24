
# ==========================================
#       SIMPLE TERMINAL BASED CALCULATOR
# ==========================================

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


# Main Calculator Program

print("====================================")
print("       WELCOME TO PYTHON CALCULATOR")
print("====================================")

while True:

    print("\nChoose an Operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "5":
        print("\nThank you for using the calculator!")
        print("Goodbye!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("\nInvalid choice! Please select between 1 and 5.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = add(num1, num2)
            operator = "+"

        elif choice == "2":
            result = subtract(num1, num2)
            operator = "-"

        elif choice == "3":
            result = multiply(num1, num2)
            operator = "*"

        elif choice == "4":
            result = divide(num1, num2)
            operator = "/"

        print("\n------------------------------------")
        print("             RESULT")
        print("------------------------------------")
        print(f"{num1} {operator} {num2} = {result}")
        print("------------------------------------")

    except ValueError:
        print("\nInvalid input! Please enter valid numbers.")
