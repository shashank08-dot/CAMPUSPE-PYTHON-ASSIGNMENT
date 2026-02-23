"""
Question 20: Number System Functions
Description: Performs conversions between different number systems.
Author: Shashank K R
"""

# -----------------------------------------
# Function: Decimal to Binary
# -----------------------------------------
def decimal_to_binary(decimal_number):
    """
    Converts a decimal number to binary
    """
    return bin(decimal_number)[2:]


# -----------------------------------------
# Function: Decimal to Octal
# -----------------------------------------
def decimal_to_octal(decimal_number):
    """
    Converts a decimal number to octal
    """
    return oct(decimal_number)[2:]


# -----------------------------------------
# Function: Decimal to Hexadecimal
# -----------------------------------------
def decimal_to_hexadecimal(decimal_number):
    """
    Converts a decimal number to hexadecimal
    """
    return hex(decimal_number)[2:].upper()


# -----------------------------------------
# Function: Binary to Decimal
# -----------------------------------------
def binary_to_decimal(binary_number):
    """
    Converts a binary number to decimal
    """
    return int(binary_number, 2)


# -----------------------------------------
# Main Program
# -----------------------------------------
try:
    # Display menu
    print("=== NUMBER SYSTEM CONVERTER ===")
    print("1. Decimal to Binary")
    print("2. Decimal to Octal")
    print("3. Decimal to Hexadecimal")
    print("4. Binary to Decimal")

    # Take user choice
    user_choice = int(input("Choose an option (1-4): "))

    # -----------------------------------------
    # Option 1: Decimal to Binary
    # -----------------------------------------
    if user_choice == 1:
        decimal_number = int(input("Enter a decimal number: "))
        print("Binary:", decimal_to_binary(decimal_number))

    # -----------------------------------------
    # Option 2: Decimal to Octal
    # -----------------------------------------
    elif user_choice == 2:
        decimal_number = int(input("Enter a decimal number: "))
        print("Octal:", decimal_to_octal(decimal_number))

    # -----------------------------------------
    # Option 3: Decimal to Hexadecimal
    # -----------------------------------------
    elif user_choice == 3:
        decimal_number = int(input("Enter a decimal number: "))
        print("Hexadecimal:", decimal_to_hexadecimal(decimal_number))

    # -----------------------------------------
    # Option 4: Binary to Decimal
    # -----------------------------------------
    elif user_choice == 4:
        binary_number = input("Enter a binary number: ")

        # Validate binary input
        if not all(digit in "01" for digit in binary_number):
            print("Invalid binary number! Only 0 and 1 allowed.")
        else:
            print("Decimal:", binary_to_decimal(binary_number))

    # -----------------------------------------
    # Invalid choice handling
    # -----------------------------------------
    else:
        print("Invalid choice! Please select between 1 and 4.")

# -----------------------------------------
# Exception handling
# -----------------------------------------
except ValueError:
    print("Invalid input! Please enter valid numeric values.")

# -----------------------------------------
# End of Program
# -----------------------------------------