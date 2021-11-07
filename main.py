import os
from art import logo


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
        print(f"The winner is {winner} with a bid of {highest_bid}")


print(logo)
no_more_bidders = False
while not no_more_bidders:
    bid_dic = {}
    name = input("What's your name?: ")
    bid = int(input("What's your bid?"))
    bid_dic[name] = bid
    another_one = input("Are there any other bidders? Type 'yes' or 'no'.")
    if another_one in ["Yes", "yes"]:
        clean = lambda: os.system('cls')
        clean()
    else:
        no_more_bidders = True
        find_highest_bidder(bidding_record = bid_dic)
