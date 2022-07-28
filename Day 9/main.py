import logo
import functions
import os

more_bids = "Y"
bids_by_name = {}

os.system("cls")
print(logo.logo)
print("Welcome to the bids game.\n")
while(more_bids == "Y"):
    functions.give_name_bid(bids_by_name)
    more_bids = input("Another bid? (Y/N)").upper()
    functions.more_bids(more_bids, bids_by_name)
