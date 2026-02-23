"""
Question 14: Factorial Calculator
Description: This program calculates the factorial of a given number
             using a loop and displays the step-by-step calculation.
Author: Shashank K R
"""

# -----------------------------------------
# Step 1: Take input safely
# -----------------------------------------

try:
    # Ask the user to enter a number
    number = int(input("Enter a number: "))

    # -----------------------------------------
    # Step 2: Validate input
    # -----------------------------------------

    # Factorial is not defined for negative numbers
    if number < 0:
        print("Factorial is not defined for negative numbers.")

    # Factorial of 0 is always 1
    elif number == 0:
        print("0! = 1")

    else:
        # Initialize factorial result and steps string
        factorial_result = 1
        steps = ""

        # -----------------------------------------
        # Step 3: Calculate factorial using loop
        # -----------------------------------------

        for i in range(number, 0, -1):
            factorial_result *= i
            steps += str(i)

            # Add multiplication symbol between numbers
            if i != 1:
                steps += " × "

        # -----------------------------------------
        # Step 4: Display result
        # -----------------------------------------

        print(f"\n{number}! = {steps} = {factorial_result}")

# -----------------------------------------
# Error handling for invalid input
# -----------------------------------------
except ValueError:
    print("Invalid input! Please enter a valid integer.")

# -----------------------------------------
# End of Program
# -----------------------------------------