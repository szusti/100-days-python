from turtle import Turtle

STARTING_POSITION:tuple = ((0,0), (-20,0), (-40,0))
MOVE_DISTANCE:int = 20
UP:int = 90
DOWN:int = 270
LEFT:int = 180
RIGHT:int = 0

class Snake:
    def __init__(self):
        self.snake_segments:list[Turtle] = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for segment in range(0,len(STARTING_POSITION)):
            one_snake_segment = Turtle(shape="square")
            one_snake_segment.color("white")
            one_snake_segment.penup()
            one_snake_segment.goto(STARTING_POSITION[segment])
            self.snake_segments.append(one_snake_segment)


    def move(self):
        """Move snake by MOVE_DISTANCE"""
        for snake_seg in range(len(self.snake_segments)-1,0,-1):
            coordinates_to_move = self.snake_segments[snake_seg-1].xcor(),self.snake_segments[snake_seg-1].ycor()
            self.snake_segments[snake_seg].goto(*coordinates_to_move)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Turn the turtle up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Turn the turtle down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Turn the turtle left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Turn the turtle right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
