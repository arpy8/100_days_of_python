from art import vs, logo
from random import *
from game_data import data

def random_person_selector():
    """selects random person from the data"""
    person = choice(data)
    return person

def game():
    print(logo)
    def article_chooser(word):
        article = "a"
        if word[0] in 'aeiouAEIOU':
            article = "an"        
        return article
    score = 0
    game_over = False
    while not game_over:
        
        random_person_a = random_person_selector()
        random_person_b = random_person_selector()

        if random_person_b == random_person_a:
            random_person_b = random_person_selector()

        print(f"Compare A: {random_person_a['name']}, {article_chooser(random_person_a['description'])} {random_person_a['description']}, from {random_person_a['country']}")
        print(vs)
        print(f"Against B: {random_person_b['name']}, {article_chooser(random_person_b['description'])} {random_person_b['description']}, from {random_person_b['country']}")
        
        user_input = input("Who has more followers? Type 'A' or 'B': ")
        if random_person_a['follower_count'] > random_person_b['follower_count']:
            if user_input == 'A' or user_input == 'a':
                score += 1
                print(f"You're right! Current score: {score}")
            elif user_input == 'B' or user_input == 'b':
                print(f"Sorry that's wrong. Final score {score}")
                game_over = True
                input()

        elif random_person_a['follower_count'] < random_person_b['follower_count']:
            if user_input == 'A' or user_input == 'a':
                print(f"Sorry that's wrong. Final score {score}")
                game_over = True
                input()
            elif user_input == 'B' or user_input == 'b':
                score += 1
                print(f"You're right! Current score: {score}")
        
        else:
            print('Invalid input.')
            input()

game()