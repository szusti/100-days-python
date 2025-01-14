from turtle import Turtle, Screen

def rotate_clockwise():
    tim.right(20)

def rotate_counter_clockwise():
    tim.left(20)

def move_forwards():
    tim.forward(20)

def move_backwards():
    tim.backward(20)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    # additionally you can use:
    # playground.resetscreen()

tim = Turtle()
playground = Screen()

playground.listen()
playground.onkey(key="a", fun=rotate_counter_clockwise)
playground.onkey(key="d", fun=rotate_clockwise)
playground.onkeypress(key="w", fun=move_forwards)
playground.onkeypress(key="s", fun=move_backwards)
playground.onkey(key="c", fun=clear_drawing)


playground.exitonclick()
