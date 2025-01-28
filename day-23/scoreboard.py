from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score:int = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-200,250)
        self.write(f"Score: {self.score}", False, "center", FONT)

    def run_over(self):
        self.goto(0,0)
        self.write(f"TURTLE IS DED. Score: {self.score}", False, "center", FONT)

    def next_round(self):
        self.goto(0,0)
        self.write("NEXT ROUND", False, "center", FONT)


