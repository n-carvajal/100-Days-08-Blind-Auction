# Imports
from art import logo
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Variables:
auction = True
bidding = True
bids = {}
max_bid = 0
max_bidder = ""
# Code
print(logo)
print("Do you want to start the auction?")
while auction:
    take_part = input("Type 'yes' or 'no': ").lower()
    if take_part == "yes":
        while bidding:
            name = input("Enter bidders name: ")
            bid = int(input("Enter bid amount: $"))
            bids[name] = bid
            print("Does anyone else want to bid?")
            another_bid = input("Type 'yes' or 'no': ").lower()
            clear_screen()
            if another_bid == "yes":
                continue
            else:
                bidding = False
        for bidder in bids:
            if bids[bidder] > max_bid:
                max_bidder = bidder
                max_bid = bids[bidder]
        print(f"The auction winner is {max_bidder} with a bid of ${max_bid}")
        print("Auction ended")
        print(logo)
        auction = False
    elif take_part == "no":
        auction = False
        print("OK. Goodbye.")
    else:
        print("That is not a valid input.")
        print("Try again.")
