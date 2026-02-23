"""
Question 7: Temperature Converter
Description: This program converts temperature values between
             Celsius, Fahrenheit, and Kelvin based on user choice.
Author: Shashank K R
"""

# ---------------------------------------
# Step 1: Display menu options
# ---------------------------------------

print("\n" + "=" * 35)
print("        TEMPERATURE CONVERTER")
print("=" * 35)
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")
print("5. Fahrenheit to Kelvin")
print("6. Kelvin to Fahrenheit")
print("7. Exit")
print("=" * 35)

# ---------------------------------------
# Step 2: Take user choice safely
# ---------------------------------------

try:
    # Read user's menu choice
    choice = int(input("Enter your choice (1-7): "))

    # If user chooses to exit
    if choice == 7:
        print("Exiting program. Thank you!")

    # Validate valid conversion choices
    elif 1 <= choice <= 6:

        # Take temperature value from user
        temperature_value = float(input("Enter temperature value: "))

        # ---------------------------------------
        # Step 3: Perform temperature conversion
        # ---------------------------------------

        # Celsius to Fahrenheit
        if choice == 1:
            result = (temperature_value * 9 / 5) + 32
            print(f"Result: {result:.2f} °F")

        # Fahrenheit to Celsius
        elif choice == 2:
            result = (temperature_value - 32) * 5 / 9
            print(f"Result: {result:.2f} °C")

        # Celsius to Kelvin
        elif choice == 3:
            result = temperature_value + 273.15
            print(f"Result: {result:.2f} K")

        # Kelvin to Celsius
        elif choice == 4:
            if temperature_value < 0:
                print("Invalid Kelvin value. Kelvin cannot be negative.")
            else:
                result = temperature_value - 273.15
                print(f"Result: {result:.2f} °C")

        # Fahrenheit to Kelvin
        elif choice == 5:
            result = (temperature_value - 32) * 5 / 9 + 273.15
            print(f"Result: {result:.2f} K")

        # Kelvin to Fahrenheit
        elif choice == 6:
            if temperature_value < 0:
                print("Invalid Kelvin value. Kelvin cannot be negative.")
            else:
                result = (temperature_value - 273.15) * 9 / 5 + 32
                print(f"Result: {result:.2f} °F")

    # If user enters an invalid menu option
    else:
        print("Invalid choice! Please select a number between 1 and 7.")

# ---------------------------------------
# Error handling for invalid input
# ---------------------------------------
except ValueError:
    print("Invalid input! Please enter numeric values only.")

# ---------------------------------------
# End of Program
# ---------------------------------------