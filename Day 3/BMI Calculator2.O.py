print("Hello and Welcome to BMI Calculator.")
weight = input("Enter  Weight in kgs : ")
height = input("Enter Height in meters : ")
float_weight = float(weight)
float_height = float(height)
bmi = float_weight / (float_height ** 2)
if bmi <= 18.5:
    print(f"You are UnderWeight.") 
elif bmi <= 25 :
    print(f"You are normal weight." )
elif bmi <= 30 :
    print(f"You are OverWeight.")
elif bmi <= 35 :
    print(f"You are Obese.")
elif bmi > 35 :
    print(f"You are Critically Obese.")
else:
    print("Invalid")
