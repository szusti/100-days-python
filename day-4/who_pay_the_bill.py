# Lesson about usage of list and random
# From list of the people, choose random person who will pay the bill for food
import random

list_of_people = ["Adam", "Ewa", "Marcin", "Ola", "Michal", "Iza"]
person_who_pay = random.choice(list_of_people)
print(f"Za obiad placi dzis - {person_who_pay}. Wyskakuj z mamony.")

#---------------------------------------
# #Different way
# number_of_people = len(list_of_people)
# # List is starting from 0, not from 1, thus the reason for minus 1
# choose_who_pay = random.randint(0,number_of_people-1)
# person_who_pay = list_of_people[choose_who_pay]
# print(f"Za obiad placi dzis - {person_who_pay}. Wyskakuj z mamony.")
