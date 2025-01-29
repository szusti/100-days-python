from turtle import Turtle
from os import path

ALLIGMENT = "center"
FONT = ("Arial", 24, "normal")
FILE_HIGHEST_SCORE = path.join(path.dirname(__file__),"data.txt")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score:int = 0
        with open(FILE_HIGHEST_SCORE) as high_score_data:
            self.high_score:int = int(high_score_data.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False,ALLIGMENT,FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(FILE_HIGHEST_SCORE,mode="w") as highest_score_data:
                # instead using str() you can use f"{}""
                highest_score_data.write(str(self.high_score))
        self.score = 0
        self.update_score_board()

    def incresse_score(self):
        self.score += 1
        self.update_score_board()

