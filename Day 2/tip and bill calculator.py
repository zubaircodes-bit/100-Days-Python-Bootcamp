# Tip and Bill Calculator
print("Hey, Welcome to the Bill Splitter and Tip Calculator")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

# Convert percentage to decimal
tip_as_percent = tip / 100

# Calculate total bill with tip
total_bill = bill + (bill * tip_as_percent)

# Split among people
total_bill_per_person = total_bill / people

# Round to 2 decimals
print(f"{round(total_bill_per_person, 2)} is the amount each person should pay")
