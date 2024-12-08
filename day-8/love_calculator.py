# You are going to write a function called calculate_love_score() that tests the compatibility between two names.  
# To work out the love score between two people: 
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   
# 2. Then check for the number of times the letters in the word LOVE occurs.   
# 3. Then combine these numbers to make a 2 digit number and print it out. 
# e.g.
# name1 = "Angela Yu" name2 = "Jack Bauer"
# T occurs 0 times 
# R occurs 1 time 
# U occurs 2 times 
# E occurs 2 times 
# Total = 5 
# L occurs 1 time 
# O occurs 0 times 
# V occurs 0 times 
# E occurs 2 times 
# Total = 3 
# Love Score = 53

def calculate_letters_occurance(word,names_list):
    score = 0
    for letter in word:
        score+=names_list.count(letter)
    return score

def calculate_love_score(names):
    true_score=calculate_letters_occurance("true",list(names))
    love_score=calculate_letters_occurance("love",list(names))
    return str(true_score)+str(love_score)

first_name = input("Provide first name ").lower()
second_name = input("Provide second name ").lower()

# For debugging
# first_name = "Kayne West".lower()
# second_name = "Kim Kardashian".lower()
result = calculate_love_score(first_name+second_name)
print(f"Your TRUE LOVE score is: {result}")