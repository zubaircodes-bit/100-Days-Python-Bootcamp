# Dont Change the Code Below
student_height = input("Input a list of student heights : ").split()
for n in range(0, len(student_height)):
  student_height[n] = int(student_height[n])
# print(student_height)
# Dont Change the Code Above
#Write your code below this row 👇
total_height = 0
for height in student_height:
  total_height += height
# print(total_height)
student = 0
for num in student_height:
  student += 1
# print(student)
average_height = round(total_height / student)
print(f"Average height is {average_height}")