# By using turtle module, draw shapes (each have one more angle). Every shape need to have different color
import turtle, random


def draw_shape(num_sides):
    one_angle = angle/angles_number
    for _ in range(num_sides):
        tim.left(one_angle)
        tim.forward(100)


angle:int = 360

tim = turtle.Turtle()
paint = turtle.Screen()
paint.colormode(255)



for angles_number in range(3,10):
    red = random.randint(1,255)
    blue = random.randint(1,255)
    yellow = random.randint(1,255)
    rgb = (red,blue,yellow)
    tim.pencolor(rgb)
    draw_shape(angles_number)

paint.exitonclick()

