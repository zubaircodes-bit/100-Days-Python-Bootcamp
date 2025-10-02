bill = input(f"Please Enter your Bill : $")
bill = float(bill)
tip = input("What Percentage of Tip do u wanna pay ? ")
tip = int(tip)
people = input("How many People are splitting the bill ? : ")
people = int(people)
bill_tip = (tip/100)*bill
# print(bill_tip)
total_bill = bill + bill_tip
print(f"Total Bill along with Tip is : {total_bill}")
split_bill = round(total_bill/people, 2)
print(f"Each Person Should Pay {split_bill}")