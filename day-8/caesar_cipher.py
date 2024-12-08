#Caesar cipher. Shift letters by specific amount of value

def cipher(text,shift):
    text_ciphered = ""
    for letter in text:
        if letter in alphabet:
            letter_position = alphabet.index(letter)
            index_shifted_letter = (shift + letter_position) % (len(alphabet))
            newletter = alphabet[index_shifted_letter]
        else:
            newletter = letter
        text_ciphered+= newletter
    print("Result: ", text_ciphered)

def encrypt(text,shift):
    cipher(text,shift)

def decrypt(text,shift):
    cipher(text,-shift)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
should_continue = True

while should_continue == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if direction == "encode":
           encrypt(text,shift)
        else:
            decrypt(text,shift)
    else:
        print("Nothing was selected")
    restart = input("Another one? y/n ")
    if restart == "n":
        should_continue = False