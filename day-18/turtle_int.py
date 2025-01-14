from turtle import Turtle, Screen
# can use alias to import, for example
# import turtle as t

tim = Turtle()
tim.shape("turtle")
tim.color("OrangeRed")

for _ in range(0,4):
    tim.forward(50)
    tim.left(90)
tim.right(90)

for _ in range(0,10):
    tim.penup()
    tim.forward(5)
    tim.pendown()
    tim.forward(5)

screen = Screen()
screen.exitonclick()
