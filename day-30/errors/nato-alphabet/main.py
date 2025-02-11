FILE_LOC = "day-30\\errors\\nato-alphabet\\nato_phonetic_alphabet.csv"

import pandas

nato_alphabet = pandas.read_csv(FILE_LOC)
nato_alphabet_dict = {row["letter"]:row["code"] for (index,row) in nato_alphabet.iterrows()}

# while True:
#     user_input = input().upper()
#     try:
#         output_list = [nato_alphabet_dict[letter] for letter in user_input]
#     except KeyError:
#         print("Please provide only latters please")
#     else:
#         break

# print(output_list)

def generate_phonetic():
    user_input = input().upper()
    try:
        output_list = [nato_alphabet_dict[letter] for letter in user_input]
    except KeyError:
        print("Please provide only latters please")
        generate_phonetic()
    else:
        print(output_list)
