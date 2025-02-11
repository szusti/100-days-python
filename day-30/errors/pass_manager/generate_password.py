#Password Generator Project
import random
LETTERS:list[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS:list[str] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS:list[str] = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
NR_LETTERS:tuple[int] = (8, 10)
NR_SYMBOLS:tuple[int] = (2, 4)
NR_NUMBERS:tuple[int] = (2, 4)

class Password:

    def __init__(self):
        self.password = ""
        """Generate random password"""
        nr_letters = random.randint(*NR_LETTERS)
        nr_symbols = random.randint(*NR_SYMBOLS)
        nr_numbers = random.randint(*NR_NUMBERS)

        password_list = []

        [password_list.append(random.choice(LETTERS)) for _ in range(nr_letters)]
        [password_list.append(random.choice(SYMBOLS)) for _ in range(nr_symbols)]
        [password_list.append(random.choice(NUMBERS)) for _ in range(nr_numbers)]

        random.shuffle(password_list)

        self.password = "".join(password_list)