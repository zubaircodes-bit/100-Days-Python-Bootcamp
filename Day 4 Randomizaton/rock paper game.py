import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
user_choice = int(input("What do you choose ? Enter 0 for Rock, 1 for Paper or 2 for Scissors : "))
computer_choice = random.randint(0,2)
if computer_choice == 0 and user_choice == 0:
    print(f" You chose {rock} and Computer chose {rock}. It is a Tie.")
elif computer_choice == 1 and user_choice == 1:
    print(f" You chose {paper} and Computer chose {paper}. It is a Tie.")
elif computer_choice == 2 and user_choice == 2:
    print(f" You chose {scissors} and Computer chose {scissors}. It is a Tie.")
elif  user_choice == 0 and computer_choice == 1 :
    print(f" You chose {rock} and Computer chose {paper}. You Lose.")
elif  user_choice == 0 and computer_choice == 2 :
    print(f" You chose {rock} and Computer chose {scissors}. You Win.")
elif  user_choice == 1 and computer_choice == 0 :
    print(f" You chose {paper} and Computer chose {rock}. You Win.")
elif  user_choice == 1 and computer_choice == 2 :
    print(f" You chose {paper} and Computer chose {scissors}. You Lose.")
elif  user_choice == 2 and computer_choice == 0 :
    print(f" You chose {scissors} and Computer chose {rock}. You Lose.")
elif  user_choice == 2 and computer_choice == 1 :
    print(f" You chose {scissors} and Computer chose {rock}. You Lose.")
else:
    print("Invalid Value.")