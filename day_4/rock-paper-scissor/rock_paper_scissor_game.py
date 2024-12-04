#Rock-paper-scissor game
import rock_paper_scissor_ascii
import random

print("Welcome to the Rock-Paper-Scissor game.\n The man vs the machine.\n  Win, or Die.\n   Let the game begin\n")
player_choice = int(input("Pick your weapon:\n0 -> Rock | 1 -> Paper | 2 -> Scissor\n"))

if -1 < player_choice < 3:
    weapons_list = [rock_paper_scissor_ascii.rock, rock_paper_scissor_ascii.paper, rock_paper_scissor_ascii.scissors]
    pc_choice = random.randint(0,2)

    print(weapons_list[player_choice])
    print(f"PC choosed: {weapons_list[pc_choice]}")
    print("------------------------------")
    if player_choice == 0:
        if pc_choice == 0:
            print("No one won")
        elif pc_choice == 1:
            print("You loosed :devil laught:")
        else:
            print("You've won \o/")

    if player_choice == 1:
        if pc_choice == 0:
            print("You've won \o/")
        elif pc_choice == 1:
            print("No one won")
        else:
            print("You loosed :devil laught:")

    if player_choice == 2:
        if pc_choice == 0:
            print("You loosed :devil laught:")
        elif pc_choice == 1:
            print("You've won")
        else:
            print("No one won")
else:
    print("Game don't have such weapon. Choose valid one")
