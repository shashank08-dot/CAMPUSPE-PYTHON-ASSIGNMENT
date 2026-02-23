"""
Question 4: Age Calculator
Description: This program calculates a person's age based on
             their birth year and converts it into different
             time units such as months, days, hours, and minutes.
Author: Shashank K R
"""

# --------------------------------------
# Import datetime module to get current year
# --------------------------------------
from datetime import datetime

# --------------------------------------
# Step 1: Take birth year safely
# --------------------------------------

try:
    # Ask the user to enter birth year
    birth_year = int(input("Enter your birth year (YYYY): "))

    # Get the current year from system date
    current_year = datetime.now().year

    # --------------------------------------
    # Step 2: Validate input
    # --------------------------------------

    # Check if birth year is in the future
    if birth_year > current_year:
        print("Birth year cannot be in the future.")

    # Check if birth year is zero or negative
    elif birth_year <= 0:
        print("Please enter a valid positive year.")

    else:
        # --------------------------------------
        # Step 3: Calculate age
        # --------------------------------------

        # Calculate age in years
        age_years = current_year - birth_year

        # Convert age into other time units
        age_months = age_years * 12
        age_days = age_years * 365       # Approximate (ignores leap years)
        age_hours = age_days * 24
        age_minutes = age_hours * 60

        # Calculate years remaining to reach 100 years
        years_until_100 = 100 - age_years

        # --------------------------------------
        # Step 4: Display results
        # --------------------------------------

        print("\n" + "=" * 35)
        print("     AGE CALCULATION RESULTS")
        print("=" * 35)

        print(f"Current age (years)      : {age_years}")
        print(f"Age in months            : {age_months}")
        print(f"Age in days (approx)     : {age_days}")
        print(f"Age in hours             : {age_hours}")
        print(f"Age in minutes           : {age_minutes}")

        # Check if the person has reached 100 years
        if years_until_100 > 0:
            print(f"Years remaining until 100: {years_until_100}")
        else:
            print("You are already 100 years or older!")

        print("=" * 35)

# --------------------------------------
# Error handling for invalid input
# --------------------------------------
except ValueError:
    print("Invalid input! Please enter a valid year in numbers.")

# --------------------------------------
# End of Program
# --------------------------------------