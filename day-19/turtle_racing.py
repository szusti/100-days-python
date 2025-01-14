# Turtle racing. Player bet which turtle (color) will be first

from turtle import Turtle, Screen
import random

COLOURS: list[str] = ["red", "orange", "yellow", "green", "blue", "purple"]
FORWARD_STEPS: tuple = (0,10)

def prepare_list_turtles(number_of_turtles: int) -> list[Turtle]:
    all_turtles = [Turtle("turtle") for _ in range(number_of_turtles)]
    prepare_state_turtles(all_turtles)
    return all_turtles

def prepare_state_turtles(all_turtles: list[Turtle]) -> None:
    highest_position_x: int = -230
    highest_position_y: int = 150
    colour:int = 0

    for turtle in all_turtles:
        turtle.penup()
        turtle.speed(3)
        turtle.color(COLOURS[colour])
        colour+=1
        turtle.setposition(highest_position_x, highest_position_y)
        highest_position_y-=50

def main() -> None:
    playground = Screen()
    playground.setup(width=500,height=400)
    all_turtles = prepare_list_turtles(6)
    user_bet = playground.textinput(title="Make your bet",prompt="Choose your turtle(color): ")
    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winnning_colour = turtle.pencolor()
                if winnning_colour == user_bet:
                    print(f"You've won. {winnning_colour} is the winner")
                else:
                    print(f"Sorry, {winnning_colour} is the winner")
            rand_distance = random.randint(*FORWARD_STEPS)
            turtle.forward(rand_distance)

    playground.exitonclick()

main()