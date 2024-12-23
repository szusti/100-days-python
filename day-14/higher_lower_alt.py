import higher_lower_data
import random
from os import system


def printPerson(personObject, followers=0):
    """Print Person details\n
    0 - everything without followers\n
    1 - name with followers\n
    anything else - only followers number"""
    if followers == 0:
        print(personObject['name'], "is a", personObject['description'], "from", personObject['country'] )
    elif followers == 1:
        print(personObject['name'], "have", personObject['follower_count'], "followers" )
    else:
        print("Number of followers", personObject['follower_count'])

def guess_higher_lower(personA, personB):
    print("Guess, who have more followers, 1, or 2")
    while True:
        more_follower_guess = int(input())
        if more_follower_guess == 1 or more_follower_guess == 2:
            break
        else:
            print("Please provide number 1 or 2")
        continue
    if personA['follower_count'] > personB['follower_count']:
        more_follower = 1
    else:
        more_follower = 2
    if more_follower == more_follower_guess:
        return True
    else:
        return False


def game():
    print("Higher or Lower")
    score = 0
    continue_game = True
    personA = random.choice(higher_lower_data.data)
    personB = 0
    while continue_game:
        while True:
            personB = random.choice(higher_lower_data.data)
            if personB['name'] != personA['name']:
                break
            else:
                continue
        ## correct = compare_persons(personA, personB)
        print(f"Current score - {score}")
        printPerson(personA)
        printPerson(personB)

        correct_guess = guess_higher_lower(personA, personB)
        system("cls")
        printPerson(personA,1 )
        printPerson(personB,1)
        if correct_guess == True:
            print("Score! You were right!")
            score+=1
            personA = personB
            print("-------------------------------------")

        else:
            print("Wrong! Your score - ", score)
            continue_game = False

game()