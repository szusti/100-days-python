import random
import hangman_ascii
import hangman_words


lives = len(hangman_ascii.stages) -1

# can be used
# from hangman_words import word_list
# thanks to the above, you don't need ot use hangman_words.word_list
chosen_word = random.choice(hangman_words.word_list)
play_more = "true"

print(hangman_ascii.logo, hangman_ascii.stages[lives])
print("Number of lives:", lives)
guess = input("Choose a letter ").lower()



display = []
for letter in chosen_word:
    display += "_"

already_guess = []

# alternatively you can define
# end_of_game = False 
# while not end_of_game 
# xxxxxx
# if "_" not in display:
#   end_of_game = True

while play_more == "true":
    all_miss = "true"
    if guess not in already_guess:
        already_guess+=guess
    for i in range(0,len(chosen_word)):
        if guess == chosen_word[i]:
            all_miss = "false"
            display[i] = guess
    print(display)
    if all_miss == "true":
        lives = lives -1
        print("you lost one live, Health: ", lives)
        print(hangman_ascii.stages[lives])
    all_miss = "true"
    if lives == 0:
        print("Game over")
        play_more = "false"
    else:
        if "_" not in display:
            play_more="false"
            print("You won \o/")
        else:
            guess = input("Choose another letter ").lower()
            from os import system
            system('cls')
            print("Already used letters\n", already_guess)
