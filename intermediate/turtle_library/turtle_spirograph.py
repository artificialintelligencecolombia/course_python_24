# Import libraries
from turtle import Turtle, Screen
import random

# Create the objects
my_pen = Turtle() # The turtle object (acts as the pen that draws lines)
my_screen = Screen() # The screen object (acts as the canvas or drawing surface)

# Configure the screen and pen
my_screen.colormode(255) # Set the color mode to RGB format for more color options
my_pen.pensize(3) # Set the thickness of the pen's line
my_pen.speed(0) # Set the drawing speed of the pen (0 is the fastest)

def draw_spirograph(circles):
    direction = 0 # Initialize the starting direction for drawing circles
    # Loop to draw the specified number of circles
    for _ in range(circles):
        # Generate a random color for the pen
        my_pen.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        # Set the pen's direction for the current circle
        my_pen.setheading(direction)
        # Draw a circle with a radius of 100 units
        my_pen.circle(100)
        # Calculate the direction for the next circle
        direction += 360 / circles

# Draw a spirograph with the specified number of circles
draw_spirograph(100)

# Keep the window open until it is clicked
my_screen.exitonclick()