"""
Question 19: Text Analysis Using Functions
Description: Analyzes a given text and displays various statistics.
Author: Shashank K R
"""

# -----------------------------------------
# Function to count total characters
# -----------------------------------------
def count_characters(text):
    """
    Returns the total number of characters
    (including spaces)
    """
    return len(text)


# -----------------------------------------
# Function to count total words
# -----------------------------------------
def count_words(text):
    """
    Splits the text into words and returns
    the total word count
    """
    words_list = text.split()
    return len(words_list)


# -----------------------------------------
# Function to count vowels
# -----------------------------------------
def count_vowels(text):
    """
    Counts vowels (a, e, i, o, u) in the text
    """
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for character in text:
        if character in vowels:
            vowel_count += 1

    return vowel_count


# -----------------------------------------
# Function to count consonants
# -----------------------------------------
def count_consonants(text):
    """
    Counts consonant letters in the text
    """
    consonant_count = 0

    for character in text:
        if character.isalpha() and character.lower() not in "aeiou":
            consonant_count += 1

    return consonant_count


# -----------------------------------------
# Function to count digits
# -----------------------------------------
def count_digits(text):
    """
    Counts numeric digits (0–9) in the text
    """
    digit_count = 0

    for character in text:
        if character.isdigit():
            digit_count += 1

    return digit_count


# -----------------------------------------
# Function to count special characters
# -----------------------------------------
def count_special_characters(text):
    """
    Counts special characters (symbols)
    excluding letters, digits, and spaces
    """
    special_count = 0

    for character in text:
        if not character.isalnum() and not character.isspace():
            special_count += 1

    return special_count


# -----------------------------------------
# Main Program
# -----------------------------------------
try:
    # Take input from user
    user_text = input("Enter a sentence for analysis: ")

    # Check for empty input
    if user_text.strip() == "":
        print("Input cannot be empty.")

    else:
        # Display analysis results
        print("\n=== TEXT ANALYSIS RESULTS ===")
        print(f"Total Characters: {count_characters(user_text)}")
        print(f"Total Words: {count_words(user_text)}")
        print(f"Total Vowels: {count_vowels(user_text)}")
        print(f"Total Consonants: {count_consonants(user_text)}")
        print(f"Total Digits: {count_digits(user_text)}")
        print(f"Total Special Characters: {count_special_characters(user_text)}")

# Handle unexpected errors safely
except Exception:
    print("An unexpected error occurred.")

# -----------------------------------------
# End of Program
# -----------------------------------------