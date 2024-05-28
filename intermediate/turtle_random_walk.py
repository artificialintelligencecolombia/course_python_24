# The script consists in creating a random walk by using turtle packages
# There's a defined length for each step.
# Each time the turtle changes its direction, it will change the color.
# The lines width is wider compared to the default width.

# Import libraries
from turtle import Turtle, Screen
import random

# Create the objects
my_pen = Turtle() # turtle obj is the 'pen' that draw lines. 
my_screen = Screen() # screen obj is the 'sheet' or canvas. Its the window.
my_pen.pensize(5) # Define the line's thickness
my_pen.speed(0) # Define the speed of the line

# Define the possible directions (angles)
directions = [0, 90, 180, 270]

# Function to move the turtle randomly
def move_turtle_randomly(steps):
    for _ in range(steps):
        # Choose a random direction
        direction = random.choice(directions)
        
        # Generates a random color for each step
        my_pen.pencolor((random.random(), random.random(), random.random()))
        
        # Turn the turtle to the chosen direction
        my_pen.setheading(direction)
        # Move the turtle forward by a specified distance
        my_pen.forward(20)

# Move the turtle randomly 50 times with each step being 50 units
move_turtle_randomly(500)

# Close the window on click
my_screen.exitonclick()
