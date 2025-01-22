from turtle import Turtle
ALLIGMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score:int = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.update_score_board()

    def update_score_board(self):
        self.write(f"Score: {self.score}", False,ALLIGMENT,FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False,ALLIGMENT,FONT)

    def incresse_score(self):
        self.score += 1
        self.clear()
        self.update_score_board()

