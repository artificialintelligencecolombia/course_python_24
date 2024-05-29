# Turtle is a python library for drawing shapes and patterns
from turtle import Turtle, Screen
import random

# Create the objects
my_pen = Turtle() # turtle obj is the 'pen' that draw lines. 
my_screen = Screen() # screen obj is the 'sheet' or canvas. Its the window.
my_screen.colormode(255)
angle = 360 # Total angle in degrees

for i in range(3, 11): # Draw shapes, starting from a triangle (3 sides) and progressing to a decagon (10 sides)
    
    # Generate the random RGB color per shape
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    my_pen.pencolor((r, g, b)) # Set the pen color to a random RGB value
    
    # Inner loop to draw each side of the polygon
    for _ in range(i):
        my_pen.forward(100)  # Move the turtle forward by 100 units
        my_pen.left(angle / i)  # Turn the turtle left by (360 / i) degrees

# Close the window on click
my_screen.exitonclick()