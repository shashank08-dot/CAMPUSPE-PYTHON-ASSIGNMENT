"""
Question 3: String Manipulator
Description: This program performs multiple string operations
             on a sentence entered by the user.
Author: Shashank K R
"""

# -------------------------------------
# Step 1: Take input from the user
# -------------------------------------

# Ask the user to enter a sentence and remove extra spaces at start and end
sentence = input("Enter a sentence: ").strip()

# -------------------------------------
# Step 2: Validate input
# -------------------------------------

# Check if the user entered an empty sentence
if sentence == "":
    print("You entered an empty sentence. Please try again.")

else:
    # -------------------------------------
    # Step 3: Perform string operations
    # -------------------------------------

    # Store original sentence
    original_sentence = sentence

    # Count characters including spaces
    characters_with_spaces = len(sentence)

    # Count characters excluding spaces
    characters_without_spaces = len(sentence.replace(" ", ""))

    # Split sentence into words
    words_list = sentence.split()

    # Count total number of words
    total_words = len(words_list)

    # Convert sentence to uppercase
    uppercase_sentence = sentence.upper()

    # Convert sentence to lowercase
    lowercase_sentence = sentence.lower()

    # Convert sentence to title case
    title_case_sentence = sentence.title()

    # Get first word
    first_word = words_list[0]

    # Get last word
    last_word = words_list[-1]

    # Reverse the entire sentence
    reversed_sentence = sentence[::-1]

    # -------------------------------------
    # Step 4: Display results
    # -------------------------------------

    print("\n" + "=" * 35)
    print("     STRING ANALYSIS RESULTS")
    print("=" * 35)

    print(f"Original sentence        : {original_sentence}")
    print(f"Characters (with spaces): {characters_with_spaces}")
    print(f"Characters (no spaces)  : {characters_without_spaces}")
    print(f"Total words             : {total_words}")
    print(f"UPPERCASE               : {uppercase_sentence}")
    print(f"lowercase               : {lowercase_sentence}")
    print(f"Title Case              : {title_case_sentence}")
    print(f"First word              : {first_word}")
    print(f"Last word               : {last_word}")
    print(f"Reversed sentence       : {reversed_sentence}")

    print("=" * 35)

# -------------------------------------
# End of Program
# -------------------------------------