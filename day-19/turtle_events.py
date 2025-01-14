# higher order function - put a function as a method parameter
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards() -> None:
    tim.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()