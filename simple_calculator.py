"""
Question 2: Simple Calculator
Description: This program performs basic arithmetic operations
             on two numbers entered by the user.
Author: Shashank K R
"""

# -----------------------------------
# Step 1: Take input safely
# -----------------------------------

try:
    # Read the first number from the user and convert to float
    first_number = float(input("Enter first number: "))

    # Read the second number from the user and convert to float
    second_number = float(input("Enter second number: "))

    # -----------------------------------
    # Step 2: Perform calculations
    # -----------------------------------

    # Addition
    addition_result = first_number + second_number

    # Subtraction
    subtraction_result = first_number - second_number

    # Multiplication
    multiplication_result = first_number * second_number

    # Exponentiation (power)
    exponent_result = first_number ** second_number

    # -----------------------------------
    # Step 3: Display results
    # -----------------------------------

    print("\n" + "=" * 30)
    print("      CALCULATOR RESULTS")
    print("=" * 30)

    print(f"{first_number} + {second_number} = {addition_result}")
    print(f"{first_number} - {second_number} = {subtraction_result}")
    print(f"{first_number} * {second_number} = {multiplication_result}")

    # Handle division and modulus carefully to avoid division by zero
    if second_number != 0:
        division_result = first_number / second_number
        modulus_result = first_number % second_number

        print(f"{first_number} / {second_number} = {division_result}")
        print(f"{first_number} % {second_number} = {modulus_result}")
    else:
        print("Division and modulus cannot be performed (division by zero).")

    print(f"{first_number} ^ {second_number} = {exponent_result}")

    print("=" * 30)

# -----------------------------------
# Error handling for invalid input
# -----------------------------------
except ValueError:
    print("Invalid input! Please enter numeric values only.")

# -----------------------------------
# End of Program
# -----------------------------------