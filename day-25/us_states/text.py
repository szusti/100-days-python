from turtle import Turtle

class Text(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_state(self,coord:tuple[int,int],state:str):
        self.goto(coord)
        self.write(arg=state,align="center",font=("Arial", 8, "normal"))