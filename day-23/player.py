from turtle import Turtle

STARTING_POSITION:tuple[int] = (0, -290)
MOVE_DISTANCE:int = 10
FINISH_LINE_Y:int = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.start_pos()

    def start_pos(self):
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)
