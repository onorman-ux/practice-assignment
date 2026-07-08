# This program intentionally violates good coding practices.

history = []
random_unused_setting = True
future_scientific_mode = False
currency_conversion_enabled = False
weather_mode = "sunny"


def do_addition_and_print_and_save_history():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    answer = x + y
    print("Result:", answer)
    history.append("The user added " + str(x) + " and " + str(y) + " and got " + str(answer))


def do_subtraction_and_print_and_save_history():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    answer = x - y
    print("Result:", answer)
    history.append("The user subtracted " + str(y) + " from " + str(x) + " and got " + str(answer))


def do_multiplication_and_print_and_save_history():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    answer = x * y
    print("Result:", answer)
    history.append("The user multiplied " + str(x) + " and " + str(y) + " and got " + str(answer))


def do_division_and_print_and_save_history():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))

    if y == 0:
        print("Error: Cannot divide by zero.")
        history.append("The user tried to divide by zero.")
    else:
        answer = x / y
        print("Result:", answer)
        history.append("The user divided " + str(x) + " by " + str(y) + " and got " + str(answer))


def print_a_lot_of_unnecessary_menu_text():
    print("\nWelcome to the calculator program.")
    print("This calculator can add numbers.")
    print("This calculator can subtract numbers.")
    print("This calculator can multiply numbers.")
    print("This calculator can divide numbers.")
    print("Maybe later it will do weather, currency, and scientific math.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Show History")
    print("6. Exit")


def useless_future_feature():
    print("This feature does nothing yet.")


while True:
    print_a_lot_of_unnecessary_menu_text()
    user_choice = input("Choose an option: ")

    if user_choice == "1":
        do_addition_and_print_and_save_history()
    elif user_choice == "2":
        do_subtraction_and_print_and_save_history()
    elif user_choice == "3":
        do_multiplication_and_print_and_save_history()
    elif user_choice == "4":
        do_division_and_print_and_save_history()
    elif user_choice == "5":
        print(history)
    elif user_choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
