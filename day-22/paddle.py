from turtle import Turtle

SHAPE_SIZE:dict={"wid":5,
                 "len":1}
PLAYERS_POS:list[tuple[int]] = [(-350,0),(350,0)]
PADDLE_MOVE_BY:int = 20

class Paddle(Turtle):
    def __init__(self,player:int):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(SHAPE_SIZE["wid"], SHAPE_SIZE["len"])
        self.color("white")
        self.start_pos(player)

    def start_pos(self,player: int):
        # -1 because list starts with index 0
        self.goto(PLAYERS_POS[player-1])

    def up(self):
        new_y = self.ycor() + PADDLE_MOVE_BY
        self.goto(self.xcor(),new_y)

    def down(self):
        new_y = self.ycor() - PADDLE_MOVE_BY
        self.goto(self.xcor(),new_y)

