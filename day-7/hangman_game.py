#The handgman game
#Special rule - do not take life when player already used letter

import random
import hangman_ascii
from hangman_words import word_list

def set_placeholder(choosen_word):
    placeholder = ""
    for amout_of_char in choosen_word:
        placeholder+="_"
    return placeholder

print(hangman_ascii.logo)
print("Welcome to the Hang-man game. You have 6 lifes to try guess proper word")
print("-----------------------------------------------------------------------")
choosen_word = random.choice(word_list)
print("DEBUG:", choosen_word)
placeholder = list(set_placeholder(choosen_word))

player_lives = 6
left_to_guess = len(choosen_word)
won = False
already_used_letters = []


while player_lives >= 0 and left_to_guess >0:
    print(placeholder,"\nLives left: ",player_lives+1, ". \nAlready tried letters -", already_used_letters)
    player_letter = input("Pick a letter ")
    if player_letter in already_used_letters:
        print("Letter was already used")
    else:
        already_used_letters.append(player_letter)
        found = False
        for letter_check in range(0,len(choosen_word)):
            if player_letter == choosen_word[letter_check]:
                placeholder[letter_check] = player_letter
                left_to_guess-=1
                found = True
        if found == False:
            print(hangman_ascii.stages[player_lives])
            player_lives-=1
            if player_lives == 0:
                print("===========\nLAST CHANCE\n===========")

if left_to_guess == 0:
    print("You've won")
else:
    print("No more lives. You've lost. The word was - ",choosen_word)




