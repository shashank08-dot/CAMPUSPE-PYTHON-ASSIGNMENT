"""
Question 9: Ticket Pricing System
Description: This program calculates the movie ticket price based on
             age category, day of the week, and number of tickets.
Author: Shashank K R
"""

# ------------------------------------------
# Step 1: Take input safely
# ------------------------------------------

try:
    # Read user inputs
    age = int(input("Enter age: "))
    day_of_week = input("Enter day of the week: ").strip().lower()
    number_of_tickets = int(input("Enter number of tickets: "))

    # ------------------------------------------
    # Step 2: Validate input
    # ------------------------------------------

    # Validate age
    if age < 0:
        print("Age cannot be negative.")

    # Validate number of tickets
    elif number_of_tickets <= 0:
        print("Number of tickets must be at least 1.")

    # Validate day of the week
    elif day_of_week not in [
        "monday", "tuesday", "wednesday", "thursday",
        "friday", "saturday", "sunday"
    ]:
        print("Invalid day entered.")

    else:
        # ------------------------------------------
        # Step 3: Determine base price per ticket
        # ------------------------------------------

        # Decide price and category based on age
        if age < 3:
            base_price = 0
            category = "Free"
        elif 3 <= age <= 12:
            base_price = 150
            category = "Child"
        elif 13 <= age <= 59:
            base_price = 300
            category = "Adult"
        else:
            base_price = 200
            category = "Senior"

        # ------------------------------------------
        # Step 4: Apply discount (weekend offer)
        # ------------------------------------------

        discount_percentage = 0

        # Apply 20% discount on weekends
        if day_of_week in ["friday", "saturday", "sunday"]:
            discount_percentage = 20

        # Calculate discount amount
        discount_amount = (base_price * discount_percentage) / 100

        # Final price per ticket after discount
        final_price_per_ticket = base_price - discount_amount

        # Total amount for all tickets
        total_amount = final_price_per_ticket * number_of_tickets

        # ------------------------------------------
        # Step 5: Display results
        # ------------------------------------------

        print("\n" + "=" * 35)
        print("        TICKET BILL DETAILS")
        print("=" * 35)

        print(f"Category                : {category}")
        print(f"Base Price per Ticket   : ₹{base_price}")
        print(f"Discount Applied        : {discount_percentage}%")
        print(f"Price After Discount    : ₹{final_price_per_ticket:.2f}")
        print(f"Number of Tickets       : {number_of_tickets}")
        print(f"Total Amount            : ₹{total_amount:.2f}")

        print("=" * 35)

# ------------------------------------------
# Error handling for invalid input
# ------------------------------------------
except ValueError:
    print("Invalid input! Please enter correct numeric values.")

# ------------------------------------------
# End of Program
# ------------------------------------------