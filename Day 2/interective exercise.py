#Write a program that adds two digits input by the user only using one input variable.
two_digit_number = input("Type a two digit number :")
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
result = int(first_digit) + int(second_digit)
print(result)