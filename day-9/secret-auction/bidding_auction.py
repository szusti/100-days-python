from bidding_art import logo
from os import system

def add_bidder():
    name = input("Provide the name of the bidder: ")
    price = round(float(input("Provide the price of your bid. Use '.' to separate decimal part of the numbers.  ")),2)
    bidders_list[name] = price

def select_winner():
    highest_bid = 0
    winning_person = ""
    for person in bidders_list:
        if bidders_list[person] > highest_bid:
            winning_person = person
            highest_bid = bidders_list[person]
    # above can be shortening with max
    # winning_person = max(bidders_list.get)
    return winning_person


print(logo)
print("Welcome to the blind bidding system")
bidders_list = {}

another_person=True

while another_person:
    add_bidder()
    add_another_person = input("Add another person? [y]/[n]: ")
    if add_another_person == "n":
        another_person=False
    system("cls")

print(bidders_list)
bid_winner = select_winner()

print(f"The winner is\n{bid_winner} : {bidders_list[bid_winner]}PLN")

