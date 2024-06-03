# Turtle is a python library for drawing shapes and patterns
from turtle import Turtle, Screen
import random

# Define the screen settings
my_screen = Screen() # screen obj is the 'sheet' or canvas. Its the window.
my_screen.setup(width=600, height=600) # Setting the screen dimensions
my_screen.bgcolor("black")
my_screen.title("My snake game")

# Define the initial position of the turtles, in column coordinates
init_positions_xaxis = [0, -20, -40]

snake_body = []

# Create the objects
for i in range(0, 3): # Six turtle objects
    new_turtle = Turtle()
    new_turtle.shape("square") 
    new_turtle.color("white") # Those are all the turtle's settings.
    new_turtle.penup()
    new_turtle.setposition(init_positions_xaxis[i], 0)
    snake_body.append(new_turtle)   

# Close the window on click
my_screen.exitonclick()