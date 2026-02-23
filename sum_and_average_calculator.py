"""
Question 13: Sum and Average Calculator
Description: This program accepts multiple numbers from the user
             and calculates the sum, average, maximum, and minimum.
Author: Shashank K R
"""

# -----------------------------------------
# Step 1: Take number count safely
# -----------------------------------------

try:
    # Ask how many numbers the user wants to enter
    number_count = int(input("How many numbers do you want to enter? "))

    # Validate number count
    if number_count <= 0:
        print("Count must be greater than zero.")

    else:
        # Initialize list and sum variable
        numbers_list = []
        total_sum = 0

        # -----------------------------------------
        # Step 2: Take numbers using a loop
        # -----------------------------------------

        for i in range(1, number_count + 1):
            number = float(input(f"Enter number {i}: "))
            numbers_list.append(number)
            total_sum += number

        # -----------------------------------------
        # Step 3: Calculate results
        # -----------------------------------------

        # Calculate average
        average = total_sum / number_count

        # Find maximum and minimum values
        maximum_number = max(numbers_list)
        minimum_number = min(numbers_list)

        # -----------------------------------------
        # Step 4: Display results
        # -----------------------------------------

        print("\n" + "=" * 35)
        print("      CALCULATION RESULTS")
        print("=" * 35)

        print(f"Sum      : {total_sum}")
        print(f"Average  : {average:.2f}")
        print(f"Maximum  : {maximum_number}")
        print(f"Minimum  : {minimum_number}")

        print("=" * 35)

# -----------------------------------------
# Error handling for invalid input
# -----------------------------------------
except ValueError:
    print("Invalid input! Please enter numeric values only.")

# -----------------------------------------
# End of Program
# -----------------------------------------