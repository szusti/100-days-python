alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
# private note - just make 2x alphabet

def caesar(plain_text,shift_amount, direction_way):
    shifted_text = ""
    # different way for if statement below. Must be above loop, not inide, otherwise it will change -- to + every two loops due to multiply two minus numbers
    # if direction_way == "decode":
    #   shift_amount *= -1
    for letter in plain_text:
        if letter not in alphabet:
            shifted_text +=letter
        else:
            index_number = alphabet.index(letter)
            if direction_way == "encode":
                shifted_text += alphabet[index_number+shift_amount]
            if direction_way == "decode":
                shifted_text += alphabet[index_number-shift_amount]
    print(direction_way ,shifted_text)

again = "true"
while again == "true":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction != "encode" and direction != "decode":
        print("Please use [encode] or [decode]")
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26
        caesar(text,shift,direction)
    repeat = input("want to use me again? [yes] or [no]\n").lower()
    if repeat == "yes":
        again = "true"
    elif repeat == "no":
        again = "false"
    else:
        print("I will take it as no")
        again = "false"


