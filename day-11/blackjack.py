import random

def start_screen():
    """Welcome page. Start screen, where player decide if he want to start new game on, or exit"""
    print("Welcome to the blackjack game")

def start_new_game():
    start_game=""
    while True:
        start_game = input("Write 'start' to start the game, or 'stop to ... you guess right, stop the game\n")
        if start_game!="start" and start_game!="stop":
            print("Please write start, or stop")
            continue
        else:
            break
    return start_game

def check_score(person_deck):
    score = 0
    for card in person_deck:
        score+=card
    return score

def draw_card(person_deck):
    """add new card to person deck"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10,10]
    select_random_card = random.randint(0,13)
    person_deck.append(cards[select_random_card])

def draw_or_pass():
    next_action = ""
    while True:
        next_action=input("'draw', or 'pass': ")
        if next_action!="draw" and next_action!="pass":
            print("please write draw, or pass\n")
            continue
        else:
            break
    return next_action

def check_ace(person_deck, player):
    if 11 in person_deck:
        change_ace(person_deck)
        if player:
            print('Your ace now will be count as 1 point instead 11')
        else:
            print("Dealer changed ace from 11 to 1 point")
        return True
    else:
        return False
def change_ace(person_deck):
    person_deck[person_deck.index(11)] = 1


def start_game():
    player_score = check_score(player_deck)
    dealer_score = check_score(dealer_deck)
    if player_score > 21:
        if check_ace(player_deck, True) == True:
            player_score = check_score(player_deck)
    print("Your cards: ", player_deck, "=", player_score, "\nDealer cards ", dealer_deck, "=", dealer_score)

    if player_score == 21:
            print("You are the King, baby, you have a perfect score of 21")
    elif player_score > 21:
            print("Looser, you've lost to Dealer")
    else:
        next_action = draw_or_pass()
        if next_action=="pass":
            draw_card(dealer_deck)
            dealer_score = check_score(dealer_deck)
            if dealer_score > 21:
                if check_ace(player_deck, False) == True:
                    dealer_score = check_score(dealer_deck)
            print("Dealer shows his cards")
            print("Dealer cards ", dealer_deck, "=", dealer_score)
            if dealer_score > 21:
                print("Nice one, Dealer went too high")
            else:
                if dealer_score >= player_score:
                    print("Looser, you've lost to Dealer")
                else:
                    print("You are the King, baby, you have won against Dealer")
        else:
            draw_card(player_deck)
            draw_card(dealer_deck)
            start_game()


start_screen()
while True:
    player_deck = []
    dealer_deck = []
    draw_card(dealer_deck)
    draw_card(player_deck)
    draw_card(player_deck)
    start_game()
    if start_new_game() == "start":
        print("Starting new game . . .\n")
        continue
    else:
        break


