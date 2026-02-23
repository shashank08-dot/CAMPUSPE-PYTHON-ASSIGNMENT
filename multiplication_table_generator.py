"""
Question 12: Multiplication Table Generator
Description: This program generates a multiplication table
             for a given number up to a specified range.
Author: Shashank K R
"""

# -----------------------------------------
# Step 1: Take input safely
# -----------------------------------------

try:
    # Read the number for which the table is required
    number = int(input("Enter number: "))

    # Read the range (end value) for the table
    range_end = int(input("Enter range (end value): "))

    # -----------------------------------------
    # Step 2: Validate input range
    # -----------------------------------------

    if range_end <= 0:
        print("Range must be greater than zero.")

    else:
        # -----------------------------------------
        # Step 3: Generate multiplication table
        # -----------------------------------------

        print("\n" + "=" * 35)
        print(f"  MULTIPLICATION TABLE OF {number}")
        print("=" * 35)

        for i in range(1, range_end + 1):
            result = number * i
            print(f"{number} x {i} = {result}")

        print("=" * 35)

# -----------------------------------------
# Error handling for invalid input
# -----------------------------------------
except ValueError:
    print("Invalid input! Please enter numeric values only.")

# -----------------------------------------
# End of Program
# -----------------------------------------