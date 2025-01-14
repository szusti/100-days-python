# By using module Turtle, make it randomly walk.
# experimenting with collections to make random function choice
#  experimenting also with some optimisations

import turtle
import random
from collections.abc import Callable

ANGLES:list[int] = [90,180,270,360]
TurtleFunction = Callable[[turtle.Turtle, int], None]
RGB_RANGE = (1,255)

def turn_left(my_turtle: turtle.Turtle, angle: int) -> None:
    my_turtle.left(angle)

def turn_right(my_turtle: turtle.Turtle, angle: int) -> None:
    my_turtle.right(angle)

def random_color(my_turtle: turtle.Turtle) -> None:
    rgb = tuple(random.randint(*RGB_RANGE) for _ in range(3))
    my_turtle.color(rgb)

# found this later. Instead complicating things, I could just use turtle.setheading() >.>
directions: dict[str, TurtleFunction] = {
    "left": turn_left,
    "right": turn_right
}

def move_turtle(my_turtle: turtle.Turtle) -> None:
    my_turtle_angle = random.choice(ANGLES)
    my_turtle_direction = random.choice(list(directions.values()))
    my_turtle_direction(my_turtle, my_turtle_angle)
    my_turtle.forward(20)



tim = turtle.Turtle()
tim.width(5)
playground = turtle.Screen()
playground.colormode(255)
loops = 50
for _ in range(0,loops):
    random_color(tim)
    move_turtle(tim)
playground.exitonclick()




