def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b


def get_numbers():
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    return first_number, second_number


def display_menu():
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")


def calculate(choice, a, b):
    if choice == "1":
        return add(a, b)
    elif choice == "2":
        return subtract(a, b)
    elif choice == "3":
        return multiply(a, b)
    elif choice == "4":
        return divide(a, b)
    else:
        return "Invalid choice."


def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "5":
            print("Goodbye!")
            break

        if choice in ["1", "2", "3", "4"]:
            num1, num2 = get_numbers()
            result = calculate(choice, num1, num2)
            print("Result:", result)
        else:
            print("Invalid option. Please try again.")


main()
