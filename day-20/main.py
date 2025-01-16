from turtle import Turtle, Screen
import snake
import time

playground = Screen()
playground.screensize(canvwidth=600, canvheight=600)
playground.bgcolor("black")
playground.title("SSSsssssssssnaaaaaaaaaake")

solid_snake = snake.Snake()
playground.tracer(0)

playground.listen()
playground.onkey(solid_snake.up,"Up")
playground.onkey(solid_snake.down,"Down")
playground.onkey(solid_snake.left,"Left")
playground.onkey(solid_snake.right,"Right")

while True:
    time.sleep(0.1)
    playground.update()
    solid_snake.move()


playground.exitonclick()