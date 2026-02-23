"""
Question 1: Personal Bio Card
Description: This program collects student details from the user
             and displays them in a neatly formatted bio card.
Author: Shashank K R
"""

# --------------------------------
# Step 1: Take student input details
# --------------------------------

# Ask the user to enter their full name
student_name = input("Enter your full name: ")

# Ask the user to enter their age
student_age = input("Enter your age: ")

# Ask the user to enter their course name
student_course = input("Enter your course: ")

# Ask the user to enter their college name
student_college = input("Enter your college name: ")

# Ask the user to enter their email address
student_email = input("Enter your email address: ")

# --------------------------------
# Step 2: Display the Bio Card
# --------------------------------

# Print a blank line and top border
print("\n" + "=" * 40)

# Print the title of the card
print("           STUDENT BIO CARD")

# Print a separator line
print("=" * 40)

# Display each detail in a formatted way
print(f"Name    : {student_name}")
print(f"Age     : {student_age} years")
print(f"Course  : {student_course}")
print(f"College : {student_college}")
print(f"Email   : {student_email}")

# Print bottom border
print("=" * 40)

# --------------------------------
# End of Program
# --------------------------------