"""
Question 17: Palindrome Checker
Description: Checks whether a given word or sentence is a palindrome.
Author: Shashank K R
"""

# -----------------------------------------
# Function to check whether text is palindrome
# -----------------------------------------

def is_palindrome(text):
    """
    This function checks if the given text is a palindrome.
    It removes spaces, converts text to lowercase,
    reverses it, and compares both strings.
    """

    # Remove spaces and convert to lowercase
    cleaned_text = text.replace(" ", "").lower()

    # Reverse the cleaned string
    reversed_text = cleaned_text[::-1]

    # Compare original and reversed text
    return cleaned_text == reversed_text


# -----------------------------------------
# Main Program
# -----------------------------------------

try:
    # Take input from user
    user_input = input("Enter a word or sentence: ")

    # Check for empty input
    if user_input.strip() == "":
        print("Input cannot be empty.")

    else:
        # Call the palindrome function
        if is_palindrome(user_input):
            print("It is a PALINDROME.")
        else:
            print("It is NOT a palindrome.")

# Handle any unexpected errors
except Exception:
    print("An unexpected error occurred.")

# -----------------------------------------
# End of Program
# -----------------------------------------