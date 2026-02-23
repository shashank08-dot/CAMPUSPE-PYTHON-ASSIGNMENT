"""
Question 5: Bill Splitter
Description: This program calculates tax, tip, total bill amount,
             and splits the final bill equally among people.
Author: Shashank K R
"""

# ----------------------------------------
# Step 1: Take input safely
# ----------------------------------------

try:
    # Read total bill amount
    total_bill_amount = float(input("Enter total bill amount: "))

    # Read number of people sharing the bill
    number_of_people = int(input("Enter number of people: "))

    # Read tax percentage
    tax_percentage = float(input("Enter tax percentage: "))

    # Read tip percentage
    tip_percentage = float(input("Enter tip percentage: "))

    # ----------------------------------------
    # Step 2: Validate inputs
    # ----------------------------------------

    # Validate bill amount
    if total_bill_amount <= 0:
        print("Bill amount must be greater than zero.")

    # Validate number of people
    elif number_of_people <= 0:
        print("Number of people must be at least 1.")

    # Validate tax and tip percentages
    elif tax_percentage < 0 or tip_percentage < 0:
        print("Tax and Tip percentages cannot be negative.")

    else:
        # ----------------------------------------
        # Step 3: Perform calculations
        # ----------------------------------------

        # Calculate tax amount
        tax_amount = (total_bill_amount * tax_percentage) / 100

        # Bill amount after adding tax
        bill_after_tax = total_bill_amount + tax_amount

        # Calculate tip amount
        tip_amount = (bill_after_tax * tip_percentage) / 100

        # Final total amount
        final_total = bill_after_tax + tip_amount

        # Amount each person has to pay
        amount_per_person = final_total / number_of_people

        # ----------------------------------------
        # Step 4: Display formatted output
        # ----------------------------------------

        print("\n" + "=" * 35)
        print("         BILL BREAKDOWN")
        print("=" * 35)

        print(f"Subtotal              : ₹{total_bill_amount:.2f}")
        print(f"Tax ({tax_percentage}%)           : ₹{tax_amount:.2f}")
        print(f"Amount after tax      : ₹{bill_after_tax:.2f}")
        print(f"Tip ({tip_percentage}%)           : ₹{tip_amount:.2f}")
        print(f"Total amount          : ₹{final_total:.2f}")
        print(f"Amount per person     : ₹{amount_per_person:.2f}")

        print("=" * 35)

# ----------------------------------------
# Error handling for invalid input
# ----------------------------------------
except ValueError:
    print("Invalid input! Please enter numeric values only.")

# ----------------------------------------
# End of Program
# ----------------------------------------