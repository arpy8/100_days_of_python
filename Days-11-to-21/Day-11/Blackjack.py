from random import *
from art import logo
from replit import *

cards  = [11,2,3,4,5,6,7,8,9,10,10,10,10,10]

def game():
    comp_cards = []
    player_cards = []

    for _ in range(2):
        comp_cards.append(choice(cards))
        player_cards.append(choice(cards))

    # print(f"computer's cards {comp_cards}")
    # print(f"player's cards {player_cards}")

    print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
    print(f"Computer's first card: {comp_cards[0]}")
    
    add_card = True
    while add_card:
        extra_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if extra_card == 'n':
            add_card = False
        elif extra_card == 'y':
            player_cards.append(choice(cards))
            comp_cards.append(choice(cards))
            print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
            print(f"Computer's first card: {comp_cards[0]}")

        if 11 in player_cards and sum(player_cards) > 21:
            player_cards.remove(11)
            player_cards.append(1)

        if sum(player_cards) > 21 and sum(comp_cards) > 21:
            print("You went over. You lose 😤")


        if sum(player_cards) == sum(comp_cards):
            print("Draw 🙃")
        elif sum(comp_cards) == 0:
            print("Lose, opponent has Blackjack 😱")
        elif sum(player_cards) == 0:
            print("Win with a Blackjack 😎")
        elif sum(player_cards) > 21:
            print("You went over. You lose 😭")
        elif sum(comp_cards) > 21:
            print("Opponent went over. You win 😁")
        elif sum(player_cards) > sum(comp_cards):
            print("You win 😃")
        else:
            print("You lose 😤")
        
    print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
    print(f"Computer's final hand: {comp_cards}, final score: {sum(comp_cards)}")
       

should_continue = True
while should_continue:
    x = input("Do you want to a play of Blackjack? Type 'y' or 'n': ")
    if x == 'n':
        should_continue = False
    elif x == 'y':
        clear()
        print(logo)
        game()
    else:
        print("Invalid input!")