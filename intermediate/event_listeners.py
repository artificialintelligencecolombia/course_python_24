# Turtle is a python library for drawing shapes and patterns
from turtle import Turtle, Screen


# Create the objects
my_pen = Turtle() # turtle obj is the 'pen' that draw lines. 
my_screen = Screen() # screen obj is the 'sheet' or canvas. Its the window.
my_pen.speed(1)

# Create a function that will be activated by the even listener
def move_forward():
    my_pen.forward(100)

my_screen.listen() # Set focus on screen object in order to collect key-events.
my_screen.onkey(fun=move_forward,key='space') # note: funs goes without parentheses ().
# TOPIC HERE: we're using FUNCTIONS AS INPUTS:
#function_a(function_b)

# Close the window on click
my_screen.exitonclick()
