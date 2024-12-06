#Program to generate random password
import random
import char_lists

num_of_letters = int(input("How many letters you want? "))
num_of_symbols = int(input("How many symbols you want? "))
num_of_numbers = int(input("How many numbers you want? "))

password = []

# NOTE - used extend function instead append. 
# Extend add elements from one list to another. Append would add list inside another list (it will be nested)
password.extend(random.choices(char_lists.letters,k=num_of_letters))
password.extend(random.choices(char_lists.symbols,k=num_of_symbols))
password.extend(random.choices(char_lists.numbers,k=num_of_numbers))
print(password)
random.shuffle(password)
print(password)

# ouput generated password in proper format
# * is unpacking, sep need to be used to remove spaces
print(*password, sep='')

# Different way With loop
# password_final = ''

# for char in password:
#     password_final +=char

# print("Pass ", password_final)


