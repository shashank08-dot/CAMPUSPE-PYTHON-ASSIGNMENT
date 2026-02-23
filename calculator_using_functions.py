"""
Question 18: Calculator Using Functions
Description: Performs basic arithmetic operations using separate functions.
Author: Shashank K R
"""

# -----------------------------------------
# Arithmetic Functions
# -----------------------------------------

def add_numbers(first_number, second_number):
    """
    Returns the sum of two numbers
    """
    return first_number + second_number


def subtract_numbers(first_number, second_number):
    """
    Returns the difference of two numbers
    """
    return first_number - second_number


def multiply_numbers(first_number, second_number):
    """
    Returns the product of two numbers
    """
    return first_number * second_number


def divide_numbers(first_number, second_number):
    """
    Returns the division result of two numbers.
    If second number is zero, returns None.
    """
    if second_number == 0:
        return None
    return first_number / second_number


# -----------------------------------------
# Main Program
# -----------------------------------------

try:
    # Display calculator menu
    print("=== SIMPLE CALCULATOR ===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Take user's operation choice
    user_choice = int(input("Choose an operation (1-4): "))

    # Validate choice
    if user_choice not in [1, 2, 3, 4]:
        print("Invalid choice! Please select between 1 and 4.")

    else:
        # Take numeric inputs
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))

        # Perform selected operation
        if user_choice == 1:
            result = add_numbers(first_number, second_number)
            print(f"Result: {result}")

        elif user_choice == 2:
            result = subtract_numbers(first_number, second_number)
            print(f"Result: {result}")

        elif user_choice == 3:
            result = multiply_numbers(first_number, second_number)
            print(f"Result: {result}")

        elif user_choice == 4:
            result = divide_numbers(first_number, second_number)

            if result is None:
                print("Error: Division by zero is not allowed.")
            else:
                print(f"Result: {result}")

# Handle invalid numeric input
except ValueError:
    print("Invalid input! Please enter numeric values only.")

# -----------------------------------------
# End of Program
# -----------------------------------------