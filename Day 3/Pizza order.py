print("Wellcome to the Pizza Shop.")
size = input("What size of Pizza Do u Want ? Small : s, Medium : m, or Large  : l : ")
pepperoni = input("Do you want Pepperoni on it ? yes : y, no : n : ")
cheese = input("Do you want Extra Cheese on it ? yes : y, no : n : ")
bill = 0

if size == "s":
    bill = 15
    if pepperoni == "y":
        bill += 2
    if cheese == "y":
        bill += 1
elif size == "m":
    bill = 20
    if pepperoni == "y":
        bill += 3
    if cheese == "y":
        bill += 1
elif size == "l":
    bill = 25
    if pepperoni == "y":
        bill += 3
    if cheese == "y":
        bill += 1
else:
    print("Invalid size selected.")
    bill = 0

print(f"your Bill is {bill}$.")
