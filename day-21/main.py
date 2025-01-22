from turtle import Screen
import snake
import time
from food import Food
from scoreboard import Scoreboard

playground = Screen()
playground.screensize(canvwidth=600, canvheight=600)
# setup is needed, because "window" in windows os =/= screen from turtle and in results scoll bard appears.
playground.setup(610,610)
playground.bgcolor("black")
playground.title("SSSsssssssssnaaaaaaaaaake")

food = Food()
solid_snake = snake.Snake()
score_board = Scoreboard()

playground.tracer(0)

playground.listen()
playground.onkey(solid_snake.up,"Up")
playground.onkey(solid_snake.down,"Down")
playground.onkey(solid_snake.left,"Left")
playground.onkey(solid_snake.right,"Right")

game_is_on = True
while game_is_on == True:
    playground.update()
    time.sleep(0.1)
    solid_snake.move()

    # Detect collistion with food.
    if solid_snake.head.distance(food) < 15:
        food.refresh()
        score_board.incresse_score()
        solid_snake.extend()

    # Detect collisions with wall
    if solid_snake.head.xcor() > 300 or solid_snake.head.xcor() < -300 or solid_snake.head.ycor() > 300 or solid_snake.head.ycor() < -300:
        game_is_on = False
        score_board.game_over()

    # Detect collision with tail - check head collision
    for segment in solid_snake.snake_segments[1:]:
        if solid_snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()


playground.exitonclick()