#Step 4

from random import *

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = choice(word_list)
word_length = len(chosen_word)
#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
lives = 6
display = []
for _ in range(word_length):
    display += "_"

while end_of_game == False:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for i in range(word_length):
        letter = chosen_word[i]
        # print(f"Current i : {i }\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[i] = letter

    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        lives -= 1 
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."

    #Join all the elements in the list and turn it into a String.

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])