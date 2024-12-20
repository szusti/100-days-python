# Number guessing game
# Guess if number is higher, or lower
# You have easy and hard mode. They differ how much attemps you have.

import random
from os import system

NUMBER_OF_LIFES = { "easy":20,
                    "medium":15,
                    "hard":10,
                    "hardcore":5,
                    "lucky":1}

def set_new_game():
    """Welcome screen, that also set difficulty and number"""
    print("Welcome to the Number Guessing Game!")
    number_to_guess = set_number()
    NUMBER_OF_LIFES = set_difficult()
    return number_to_guess, NUMBER_OF_LIFES

def set_difficult():
    difficult = ""
    while difficult not in NUMBER_OF_LIFES:
        print("Choose difficult -",*NUMBER_OF_LIFES)
        difficult = input()
    return NUMBER_OF_LIFES[difficult]

def set_number():
    number_range = 100
    print(f"I'm thinking of a number between 1 and {number_range}")
    return random.randint(1,number_range)

def check_number(number_to_guess, user_guess):
    if user_guess < number_to_guess:
        return "higher"
    elif user_guess > number_to_guess:
        return "lower"
    else:
        return "match"

def game():
    number_to_guess, players_life = set_new_game()
    while players_life > 0:
        try:
            user_guess = int(input("Enter your guess: "))
            result = check_number(number_to_guess, user_guess)
            if result == "match":
                print("Congratulations! You've guessed the number! \o/")
                break
            else:
                players_life -= 1
                if players_life > 0:
                    print(f"Lives remaining: {players_life}")
                    print(f"Try {result}.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print(f"Game over! The number was {number_to_guess}.")

another_game = True
while another_game:
    system('cls')
    game()
    answers_to_continue = {"yes":True,
                           "no":False}
    start_another_game = ""
    while start_another_game not in answers_to_continue:
        start_another_game = input ("Do you want to start another game? [yes]/[no]")
    another_game = answers_to_continue[start_another_game]
