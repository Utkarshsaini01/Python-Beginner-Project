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

components = [rock, paper, scissors]

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))


computer = random.randint(0, 2)

print("Your choice: \n")
print(components[user])

print("\nComputer chose: \n")
print(components[computer])

if(user == computer):
    print("Draw")
elif(user == 0 and computer == 2):
    print("You Win")
elif(user == 2 and computer == 1):
    print("You Win")
elif(user == 1 and computer == 0):
    print("You Win")
else:
    print("You lose")

