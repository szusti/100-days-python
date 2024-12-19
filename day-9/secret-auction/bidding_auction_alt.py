import os
import bidding_art

print("Witaj w mini programie licytowym", bidding_art.logo)

def add_new_bidder(name, bid):
    bidders_list.update({ name: bid})

def check_who_won():
    highest_bid = ["Nowak",0] 
    
    for next_bidder in bidders_list:
        if bidders_list[next_bidder] > highest_bid[1]:
            highest_bid[0] = next_bidder
            highest_bid[1] = bidders_list[next_bidder]
    print(f"Licytacje wygral {highest_bid}")


bidders_list = {}
more_bidders = True

while more_bidders:
    name = input("Podaj swoje imie\n")
    bid = int(input("Podaj swoja kwote\n"))
    add_new_bidder(name, bid)
    next_bidder = "placeholder"
    while next_bidder != "t" and next_bidder != "n":
        next_bidder = input("Czy ktos jeszcze licytuje?\n[t]ak, [n]ie\n").lower()
    if next_bidder == "n":
        more_bidders = False
    os.system('cls')

check_who_won()