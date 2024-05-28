# Import libraries
from turtle import Turtle, Screen
import random

# Create the objects
my_pen = Turtle() # turtle obj is the 'pen' that draw lines. 
my_screen = Screen() # screen obj is the 'sheet' or canvas. Its the window.

# Define the features of the objects
my_screen.colormode(255) # Set the color mode to rgb format
my_pen.pensize(3) # Define the line's thickness
my_pen.speed(0) # Define the speed of the line

def draw_spirograph(circles):
    direction = 0 # Set the initial circle's direction
    # Iterates over each circle
    for _ in range(circles):
        
        # Generates a random color for each step
        my_pen.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        my_pen.setheading(direction) # Turn the turtle to the chosen direction
        my_pen.circle(100) # Draw the circle
        direction += 360/circles # Set the next circle's direction

# Create the spirograph with n circles
draw_spirograph(100)

# Close the window on click
my_screen.exitonclick()