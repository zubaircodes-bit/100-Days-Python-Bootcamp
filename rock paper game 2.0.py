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
user_choice = int(input("What do you choose ? Enter 0 for Rock, 1 for Paper or 2 for Scissors : "))
images = [rock, paper, scissors]
if user_choice >= 3 or user_choice < 0 :
    print("You typed an invalid number, you lose!")
else:
    print(images[user_choice])
computer_choice = random.randint(0,2)
print("Computer chose:")
print(images[computer_choice])
if user_choice == 0 and computer_choice == 2:
    print("You Win.")
elif computer_choice == 0 and user_choice == 2:
    print("You Lose.")
elif computer_choice > user_choice : 
    print("You lose")
elif user_choice > computer_choice :
    print("You Win")
elif computer_choice == user_choice :
    print("It is a Tie.")
else:
    print("invalid")
    