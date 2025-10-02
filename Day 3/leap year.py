year = int(input("Please enter ur year : "))
if year % 4 == 0 :
    if year % 100 != 0:
        print("Your Year is a leap year.")
    elif year % 400 == 0:
        print("Your Year is a leap year.")
    else:
        print("Your Year is not a leap year.")