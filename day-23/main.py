import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

NUMBER_OF_CARS:int = 25
# Make different cars position each round.
EACH_ROUND_DIFFERENT:bool = True
# MAKE each car move at random speed
DYNAMIC_MOVEMENT_CAR:bool = True

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("grey")
screen.tracer(0)
screen.listen()

player:Player = Player()
screen.onkeypress(player.move_up,"Up")

scoreboard = Scoreboard()

list_of_cars:list[CarManager] = []
[list_of_cars.append(CarManager(DYNAMIC_MOVEMENT_CAR)) for _ in range(NUMBER_OF_CARS)]


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in list_of_cars:
        car.drive()
        if car.distance(player) < 25:
            game_is_on = False
    if player.ycor() >= 300:
        scoreboard.score += 1
        scoreboard.update_score()
        player.start_pos()
        scoreboard.next_round()
        screen.update()
        time.sleep(2)
        scoreboard.update_score()
        # This is to make each round different - different cars position.
        if EACH_ROUND_DIFFERENT:
            # First, you need to hide cars, otherwise old ones will be visible
            [car.hideturtle() for car in list_of_cars]
            list_of_cars.clear()
            [list_of_cars.append(CarManager(DYNAMIC_MOVEMENT_CAR)) for _ in range(NUMBER_OF_CARS)]


scoreboard.run_over()

screen.exitonclick()
