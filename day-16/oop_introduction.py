
# Introduction to the object oriented programming (OOP) by using Turtle - graphic package
# NOTE. additional packages can be installed in command line (if pytho installed) via 
# py -m install <package name>
# to remove, just use uninstall instead install

import turtle
## Alternative
from turtle import Turtle, Screen

robert = turtle.Turtle()
#thanks to the alternative import
henry = Turtle()
henry.color('black', 'green')
henry.shape("turtle")
print(henry)
henry.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()