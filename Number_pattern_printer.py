"""
Question 11: Number Pattern Printer
Description: This program prints different number patterns
             based on the user's choice and given height.
Author: Shashank K R
"""

# -----------------------------------------
# Step 1: Take input safely
# -----------------------------------------

try:
    # Display pattern menu
    print("\n" + "=" * 35)
    print("       NUMBER PATTERN PRINTER")
    print("=" * 35)
    print("1. Pattern 1 (Increasing numbers)")
    print("2. Pattern 2 (Repeated numbers)")
    print("3. Pattern 3 (Reverse numbers)")
    print("4. Pattern 4 (Number Pyramid)")
    print("=" * 35)

    # Take user inputs
    pattern_choice = int(input("Enter pattern number (1-4): "))
    height = int(input("Enter height: "))

    # -----------------------------------------
    # Step 2: Validate input
    # -----------------------------------------

    if height <= 0:
        print("Height must be greater than zero.")

    # -----------------------------------------
    # Pattern 1: Increasing numbers
    # -----------------------------------------
    elif pattern_choice == 1:
        for i in range(1, height + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()

    # -----------------------------------------
    # Pattern 2: Repeated numbers
    # -----------------------------------------
    elif pattern_choice == 2:
        for i in range(1, height + 1):
            for j in range(i):
                print(i, end=" ")
            print()

    # -----------------------------------------
    # Pattern 3: Reverse numbers
    # -----------------------------------------
    elif pattern_choice == 3:
        for i in range(height, 0, -1):
            for j in range(i, 0, -1):
                print(j, end=" ")
            print()

    # -----------------------------------------
    # Pattern 4: Number Pyramid
    # -----------------------------------------
    elif pattern_choice == 4:
        for i in range(1, height + 1):
            # Print leading spaces
            for space in range(height - i):
                print(" ", end="")

            # Print increasing numbers
            for num in range(1, i + 1):
                print(num, end="")

            # Print decreasing numbers
            for num in range(i - 1, 0, -1):
                print(num, end="")

            print()

    # -----------------------------------------
    # Invalid pattern selection
    # -----------------------------------------
    else:
        print("Invalid pattern choice. Please select between 1 and 4.")

# -----------------------------------------
# Error handling for invalid input
# -----------------------------------------
except ValueError:
    print("Invalid input! Please enter numeric values only.")

# -----------------------------------------
# End of Program
# -----------------------------------------