import random
import os

DIFFICULT = { "easy":20,
             "medium":15,
             "hard":10,
             "hardcore":5,
             "test your luck":1}

def check_guess(number_to_guess):
    '''Checks if user provided too high, too low, or perfect number, Returns low, high or match'''
    while True:
        try:
            user_think = int(input("Make a guess: "))
        except ValueError:
            print("Sorry, this is not a valid number")
            continue
        if user_think > 0 and user_think < 100:
            break
        else:
            print("Invalid number. It must be between 0 - 100")
            continue
    if number_to_guess > user_think:
        print("Too low")
        return False
    elif number_to_guess < user_think:
        print("Too high")
        return False
    else:
        print("!!!Match!!!")
        return True


def start_page():
    '''Start up screen. Show welcome message, ad make user selected difficult'''
    os.system('cls')
    print("Welcome to the Guess, where you need to guess number between 0 to 100\nSelect difficult:")
    for keys in DIFFICULT:
        print(keys, end="|")
    print("")
    while True:
        selected_difficult = input()
        if selected_difficult in DIFFICULT:
            selected_difficult = DIFFICULT.get(selected_difficult)
            print(f"You have: {selected_difficult} number of tries")
            break
        else:
            print("Please provide valid difficult")
    return selected_difficult

def game():
    num_of_tries = start_page()
    number_to_guess = random.randint(0,100)
    next_guess = True
    while next_guess:
        guess_result = check_guess(number_to_guess)
        if guess_result == True:
            print("It's match! You've won the game \o/")
            next_guess = False
        else:
            num_of_tries-=1
            if num_of_tries == 0:
               print(f"You've lost the game. The number was {number_to_guess}")
               next_guess = False
            else:
              print(f"You still have {num_of_tries} attempts")
    next_game = input("Want to continue? y/n: ")
    if next_game == "y":
        game()

game()