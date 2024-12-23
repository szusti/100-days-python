# Game where you guess who have more followers on cosial media.
# You keep going gathering point for each proper guess till you guess wrong

from higher_lower_data import data
import random

def welcome_screen():
    welcome_message="""
                    Welcome to the game
You will see two people. Your task it to guess who have more followers.
For each proper guess you will get 1 point. Guess wrong and it's game over
Try to get as high score as possible
Have fun :)

"""
    print(welcome_message)

def choose_person():
    """Choose two persons to compare"""
    return random.sample(data,2)

def print_nice_without_followers(person):
    """print random selected persons without showing followers"""
    print(f"Person:{person['name']}. He/She is a {person['description']} from {person['country']}.")

def print_nice_followers(person):
    print(f"{person['name']} have {person['follower_count']}")

def player_selection():
    """Player choose which person he believe have more followers"""
    options =  {"1":"First person",
                "2":"Second person"}
    for key,value in options.items():
        print(f"Type {key}, for {value}")
    while True:
        choice = input("Choose which one: ")
        if choice in options:
            return int(choice)
        else:
            print("Please write 1, or 2")

def check_guess(player_guess, persons_to_compare):
    """Check if player guess right"""
    print_nice_followers(persons_to_compare[0])
    print_nice_followers(persons_to_compare[1])
    player_guess -=1
    more_followers = -1
    person_1= int(persons_to_compare[0]["follower_count"])
    person_2= int(persons_to_compare[1]["follower_count"])
    if  person_1 > person_2:
        more_followers = 0
    else:
        more_followers = 1
    if player_guess == more_followers:
        print(f"You guess right \o/")
        return True
    else:
        print("Wrong!. ＞﹏＜")
        return False


def game():
    welcome_screen()
    player_score=0
    while True:
        print("Who have more followers?")
        print("-------------------------------")
        persons_to_compare = choose_person()
        print_nice_without_followers(persons_to_compare[0])
        print("-------------OR--------------")
        print_nice_without_followers(persons_to_compare[1])
        print("-------------------------------")
        player_choice = player_selection()
        print("\n")
        answer_was_right = check_guess(player_choice,persons_to_compare)
        if answer_was_right:
            player_score+=1
            print(f"Let's goooooooooooooo, successfull streak {player_score}\n\n")
        else:
            print(f"Your end score - {player_score}")
            break

game()