"""
Question 6: Grade Calculator
Description: This program calculates the total marks, percentage,
             grade, and pass/fail result based on marks obtained
             in five subjects.
Author: Shashank K R
"""

# ----------------------------------------
# Step 1: Take input safely
# ----------------------------------------

try:
    # Read marks for each subject
    subject1_marks = float(input("Enter marks for Subject 1: "))
    subject2_marks = float(input("Enter marks for Subject 2: "))
    subject3_marks = float(input("Enter marks for Subject 3: "))
    subject4_marks = float(input("Enter marks for Subject 4: "))
    subject5_marks = float(input("Enter marks for Subject 5: "))

    # ----------------------------------------
    # Step 2: Store and validate marks
    # ----------------------------------------

    # Store all marks in a list
    marks_list = [
        subject1_marks,
        subject2_marks,
        subject3_marks,
        subject4_marks,
        subject5_marks
    ]

    # Check if any mark is outside the valid range (0 to 100)
    if any(mark < 0 or mark > 100 for mark in marks_list):
        print("Marks must be between 0 and 100.")

    else:
        # ----------------------------------------
        # Step 3: Calculate total and percentage
        # ----------------------------------------

        # Calculate total marks
        total_marks = sum(marks_list)

        # Calculate percentage
        percentage = (total_marks / 500) * 100

        # ----------------------------------------
        # Step 4: Determine grade based on percentage
        # ----------------------------------------

        if percentage >= 90:
            grade = "A+ (Outstanding)"
        elif percentage >= 80:
            grade = "A (Excellent)"
        elif percentage >= 70:
            grade = "B (Good)"
        elif percentage >= 60:
            grade = "C (Average)"
        elif percentage >= 50:
            grade = "D (Pass)"
        else:
            grade = "F (Fail)"

        # ----------------------------------------
        # Step 5: Determine pass/fail result
        # ----------------------------------------

        # Student must score at least 40 in each subject to pass
        if all(mark >= 40 for mark in marks_list):
            result = "PASS"
        else:
            result = "FAIL"

        # ----------------------------------------
        # Step 6: Display results
        # ----------------------------------------

        print("\n" + "=" * 35)
        print("           GRADE REPORT")
        print("=" * 35)

        print(f"Total Marks : {total_marks} / 500")
        print(f"Percentage  : {percentage:.2f}%")
        print(f"Grade       : {grade}")
        print(f"Result      : {result}")

        print("=" * 35)

# ----------------------------------------
# Error handling for invalid input
# ----------------------------------------
except ValueError:
    print("Invalid input! Please enter numeric marks only.")

# ----------------------------------------
# End of Program
# ----------------------------------------