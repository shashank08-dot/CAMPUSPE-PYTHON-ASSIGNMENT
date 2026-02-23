"""
Question 16: Number Guessing Game
Description: User guesses a randomly generated number within limited attempts.
Author: Shashank K R
"""

import random

# -----------------------------------------
# Main game loop (runs until user exits)
# -----------------------------------------

while True:
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Initialize attempt counters
    attempts_remaining = 7
    attempts_used = 0

    print("\n=== NUMBER GUESSING GAME ===")
    print("Guess the number between 1 and 100.")
    print("You have 7 attempts.\n")

    # -----------------------------------------
    # Guessing loop
    # -----------------------------------------

    while attempts_remaining > 0:
        try:
            # Take user input
            guess = int(input("Enter your guess: "))
            attempts_used += 1

            # Validate input range
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            # Check the guess
            if guess == secret_number:
                print(f"\n🎉 Congratulations!")
                print(f"You guessed the number correctly in {attempts_used} attempts.")
                break

            elif guess < secret_number:
                print("Too low!")

            else:
                print("Too high!")

            # Decrease remaining attempts
            attempts_remaining -= 1
            print(f"Attempts remaining: {attempts_remaining}\n")

        # Handle invalid (non-numeric) input
        except ValueError:
            print("Invalid input! Please enter a valid number.\n")

    # -----------------------------------------
    # If user fails to guess the number
    # -----------------------------------------

    if attempts_remaining == 0 and guess != secret_number:
        print(f"\n❌ Game Over!")
        print(f"The correct number was {secret_number}.")

    # -----------------------------------------
    # Ask user if they want to play again
    # -----------------------------------------

    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()

    if play_again != "yes":
        print("\nThank you for playing! 😊")
        break

# -----------------------------------------
# End of Program
# -----------------------------------------