from random import*
choice = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

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
rpsList = [rock, paper, scissors] 
compChoice = randint(0,2)
print(rpsList[choice], "\nComputer chose:\n", rpsList[compChoice])
if choice == 0 and compChoice == 1:
    print("You lose")    
elif choice == 0 and compChoice == 2: 
    print("You win")
elif choice == 1 and compChoice == 2:
    print("You lose")
elif choice == 1 and compChoice == 0:
    print("You win")
elif choice == 2 and compChoice == 0:
    print("You lose")
elif choice == 2 and compChoice == 1:
    print("You win")
else: 
    print("Tie")