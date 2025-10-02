# We had to find life left in days, weeks, and months if u were going to live till 90.
# Then we had to find out how many days, weeks, and months we have lived till now.
# Finally we had to subtract the two to find out how many days, weeks, and months we have left.
print("Welcome to the Life Calculator.")
left_life_in_days = 90 * 365 
left_life_in_weeks = 90 * 52
left_life_in_months = 90 * 12
age = input("What is your current age? ")
age_as_int = int(age)
age_in_weeks = age_as_int * 52
age_in_days = age_as_int * 365
age_in_months = age_as_int * 12
print(f"Your age in weeks is {age_in_weeks}, in days is {age_in_days} and in months is {age_in_months}.")
print(f"Calculating your remaining life...")
print(f"You have {left_life_in_days - age_in_days} days, {left_life_in_weeks - age_in_weeks} weeks, and {left_life_in_months - age_in_months} months left.")