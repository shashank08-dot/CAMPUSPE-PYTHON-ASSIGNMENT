"""
Question 8: Leap Year Checker
Description: This program checks whether a given year is a leap year
             and clearly explains the reason based on leap year rules.
Author: Shashank K R
"""

# ----------------------------------------
# Step 1: Take input safely
# ----------------------------------------

try:
    # Ask the user to enter a year
    year = int(input("Enter a year: "))

    # ----------------------------------------
    # Step 2: Validate input
    # ----------------------------------------

    # Year must be a positive number
    if year <= 0:
        print("Please enter a valid positive year.")

    else:
        # ----------------------------------------
        # Step 3: Check leap year conditions
        # ----------------------------------------

        # Leap year rules:
        # 1. Year must be divisible by 4
        # 2. If divisible by 100, it must also be divisible by 400

        if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
            print(f"\n{year} is a LEAP year.")

            # Explain the reason
            if year % 400 == 0:
                print("Reason: It is divisible by 400.")
            elif year % 100 == 0:
                print("Reason: It is divisible by 100 but also divisible by 400.")
            else:
                print("Reason: It is divisible by 4 but not divisible by 100.")

        else:
            print(f"\n{year} is NOT a leap year.")

            # Explain why it is not a leap year
            if year % 4 != 0:
                print("Reason: It is not divisible by 4.")
            elif year % 100 == 0 and year % 400 != 0:
                print("Reason: It is divisible by 100 but not divisible by 400.")

# ----------------------------------------
# Error handling for invalid input
# ----------------------------------------
except ValueError:
    print("Invalid input! Please enter a numeric year.")

# ----------------------------------------
# End of Program
# ----------------------------------------