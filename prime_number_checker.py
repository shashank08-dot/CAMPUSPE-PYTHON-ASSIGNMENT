"""
Question 15: Prime Number Checker
Description: This program checks whether a given number is prime
             and also prints all prime numbers within a given range.
Author: Shashank K R
"""

# -----------------------------------------
# Function to check if a number is prime
# -----------------------------------------

def is_prime(number):
    """
    This function returns True if the number is prime,
    otherwise returns False.
    """
    # Numbers less than or equal to 1 are not prime
    if number <= 1:
        return False

    # 2 is the only even prime number
    if number == 2:
        return True

    # Check divisibility from 2 to square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


# -----------------------------------------
# Part 1: Check if a single number is prime
# -----------------------------------------

try:
    # Take input from user
    user_number = int(input("Enter a number to check if it is prime: "))

    # Check and display result
    if is_prime(user_number):
        print(f"{user_number} is a PRIME number.")
    else:
        print(f"{user_number} is NOT a prime number.")

    # -----------------------------------------
    # Part 2: Find prime numbers in a given range
    # -----------------------------------------

    start_range = int(input("\nEnter start range: "))
    end_range = int(input("Enter end range: "))

    # Validate range
    if start_range > end_range:
        print("Start range must be less than or equal to end range.")
    else:
        print("\nPrime numbers in the given range:")

        # Loop through the range and print prime numbers
        for num in range(start_range, end_range + 1):
            if is_prime(num):
                print(num, end=" ")

# -----------------------------------------
# Error handling for invalid input
# -----------------------------------------
except ValueError:
    print("Invalid input! Please enter valid integers only.")

# -----------------------------------------
# End of Program
# -----------------------------------------