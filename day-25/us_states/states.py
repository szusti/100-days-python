import csv

STATES_FILES:str = "day-25\\us_states\\50_states.csv"
class State:

    def __init__(self):
        self.states_dict:dict[str:int,int] = self.load_states()
        self.guessed_states:list[str] = []

    def load_states(self):
        states_dict = {}
        with open(STATES_FILES) as file:
            csv_reader = csv.reader(file)
            # next() tells iterator how many first iterations to skip. So, by using 2x next, he will ignore first two iterations
            next(csv_reader)
            for row in csv_reader:
                state, x, y = row
                states_dict[state] = (int(x), int(y))
        return states_dict

    def get_coordinates(self, state:str):
        """ return coordinations (x,y), or False if already guessed or not found. """
        guess = self.states_dict.get(state, False)
        if guess == False or state in self.guessed_states:
            return False
        else:
            self.guessed_states.append(state)
            return guess