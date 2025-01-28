from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE:int = 5
MOVE_INCREMENT:int = 10
MOVE_INCREMENT_DYNAMIC:tuple[int] = (5,15)


class CarManager(Turtle):

    def __init__(self, dynamic_speed: bool):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.color(random.choice(COLORS))
        self.set_position()
        self.setheading(180)
        if dynamic_speed:
            self.move_distance = random.randint(*MOVE_INCREMENT_DYNAMIC)
        else:
            self.move_distance = STARTING_MOVE_DISTANCE

    def set_position(self):
        y_pos = random.randint(-250,300)
        x_pos = random.randint(-250,300)
        self.goto(x_pos,y_pos)

    def drive(self):
        self.forward(self.move_distance)
        if self.xcor() < -300:
            self.goto(300,self.ycor())

