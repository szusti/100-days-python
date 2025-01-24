from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=610,width=810)
screen.screensize(canvheight=600,canvwidth=800)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)
scoreboard = Scoreboard()

l_paddle = Paddle(1)
r_paddle = Paddle(2)
ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.up,"Up")
screen.onkeypress(r_paddle.down,"Down")
screen.onkeypress(l_paddle.up,"w")
screen.onkeypress(l_paddle.down,"s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 335 or ball.distance(l_paddle) < 50 and ball.xcor() < -335:
        ball.bounce_x()

    if ball.xcor() > 350:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_score()
    if ball.xcor() < -350:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update_score()



screen.exitonclick()