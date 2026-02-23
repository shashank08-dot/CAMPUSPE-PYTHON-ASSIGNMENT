"""
Question 10: Simple ATM Simulator
Description: This program simulates basic ATM operations such as
             checking balance, depositing money, and withdrawing money.
Author: Shashank K R
"""

# ---------------------------------------
# Step 1: Initialize account balance
# ---------------------------------------

account_balance = 10000  # Initial balance in the account (₹)

# ---------------------------------------
# Step 2: Start ATM menu loop
# ---------------------------------------

while True:
    print("\n" + "=" * 30)
    print("        ATM SIMULATOR")
    print("=" * 30)
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print("=" * 30)

    try:
        # Take user choice
        user_choice = int(input("Enter your choice (1-4): "))

        # ---------------------------------------
        # Option 1: Check Balance
        # ---------------------------------------
        if user_choice == 1:
            print(f"Current Balance: ₹{account_balance}")

        # ---------------------------------------
        # Option 2: Deposit Money
        # ---------------------------------------
        elif user_choice == 2:
            deposit_amount = float(input("Enter amount to deposit: "))

            if deposit_amount <= 0:
                print("Deposit amount must be greater than zero.")
            else:
                account_balance += deposit_amount
                print("Deposit successful!")
                print(f"Updated Balance: ₹{account_balance}")

        # ---------------------------------------
        # Option 3: Withdraw Money
        # ---------------------------------------
        elif user_choice == 3:
            withdraw_amount = float(input("Enter amount to withdraw: "))

            if withdraw_amount <= 0:
                print("Withdrawal amount must be greater than zero.")

            elif withdraw_amount > account_balance:
                print("Insufficient balance.")

            elif account_balance - withdraw_amount < 500:
                print("Minimum balance of ₹500 must be maintained.")

            else:
                account_balance -= withdraw_amount
                print("Withdrawal successful!")
                print(f"Updated Balance: ₹{account_balance}")

        # ---------------------------------------
        # Option 4: Exit ATM
        # ---------------------------------------
        elif user_choice == 4:
            print("Thank you for using the ATM. Goodbye!")
            break

        # ---------------------------------------
        # Invalid menu choice
        # ---------------------------------------
        else:
            print("Invalid choice! Please select between 1 and 4.")

    # ---------------------------------------
    # Error handling for invalid input
    # ---------------------------------------
    except ValueError:
        print("Invalid input! Please enter numeric values only.")

# ---------------------------------------
# End of Program
# ---------------------------------------