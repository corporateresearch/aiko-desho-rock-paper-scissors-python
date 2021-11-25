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

user = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

if user == "0":
  print(rock)
elif user == "1":
  print(paper)
elif user == "2":
  print(scissors)

computer = ["0", "1", "2"]
computer = random.randint(0,2)
print(computer)
if computer == 0:
  print(rock)
elif computer == 1:
  print(paper)
elif computer == 2:
  print(scissors)

if user == "0" and computer == 0:
  print("Draw")
elif user == "1" and computer == 1:
  print("Draw")
elif user == "2" and computer == 2:
  print("Draw")
elif user == "0" and computer == 2:
  print("You win!")
elif user == "2" and computer == 1:
  print("You win!")
elif user == "1" and computer == 0:
  print("You win!")
else:
  print("You lose!")