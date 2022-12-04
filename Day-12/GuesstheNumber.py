from random import *
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

rand_num = randint(1,100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    lives = 10
elif difficulty == 'hard':
    lives = 5
else:
    print("invalid input")

should_continue = True

while should_continue:
    print(f"You have {lives} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    if lives != 0:
        if user_guess != rand_num:
            if user_guess < rand_num:
                print("Too low.\nGuess again.")
                lives -= 1
            elif user_guess > rand_num:
                print("Too high.\nGuess again.")
                lives -= 1
        elif user_guess == rand_num:
            print(f"You got it. The answer was {rand_num}")
            should_continue = False
    elif lives == 0:
        print("You've run out of guesses, you lose.")
        should_continue = False