from os import path
from letter import Letter

working_dir = path.dirname(__file__)
location_with_names = (path.join(working_dir,"Input\\Names\\","invited_names.txt"))
with open(location_with_names) as file_with_names:
    list_of_names:list[str] = file_with_names.readlines()

for name in list_of_names:
    letter = Letter(name.strip())


# this can be done in less complicated way (without separated class), but for learning purposes I've decided to make this different.
# From video simplyfied way
# NOTE those relative path might not work becase of how program that you use interpret relative path

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
