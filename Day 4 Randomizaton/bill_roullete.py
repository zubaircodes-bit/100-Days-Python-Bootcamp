import random
names_string = input("Enter Your Names Separated by Commas : ")
names = [name.strip() for name in names_string.split(",")]
# print(names_string)
# print(names)
names_len = len(names)
random_person = random.randint(0, names_len - 1)
print(f"{names[random_person]} is going to pay the bill!")