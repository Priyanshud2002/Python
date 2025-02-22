print("Welcome to the tip calculator!")

# Get user inputs
total_bill = float(input("How much was the total bill? "))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
contri = int(input("How many people to split the bill? "))

# Calculate the total bill including tip
tip_amount = (tip_percentage / 100) * total_bill
total_amount = total_bill + tip_amount

# Split the bill
each_person = total_amount / contri

# Display the result
print(f"Each person should pay: ${each_person:.2f}")
