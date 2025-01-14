import turtle
import random

# Create a turtle object
t = turtle.Turtle()

# Define the dictionary with the turtle's turning functions
directions = {
    "left": t.left,
    "right": t.right
}

# Choose a random direction and angle
direction = random.choice(list(directions.keys()))
angle = random.randint(0, 360)

# Make the turtle turn
directionsdirection

# Keep the window open until it is closed by the user
turtle.done()