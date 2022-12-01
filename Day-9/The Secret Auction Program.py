from replit import clear
from art import logo

print(logo)

mydict = {}
     
should_continue = True

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of, ${highest_bid}")

while should_continue:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    mydict[name] = bid
    x = input("are there any other who wants to bid? ")
    if x == 'no':
        should_continue = False
        find_highest_bidder(mydict)
    elif x == "yes":
        clear()
