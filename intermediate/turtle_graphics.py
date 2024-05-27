# Turtle is a python library for drawing shapes and patterns
from turtle import Turtle, Screen


# Create the objects
my_pen = Turtle() # turtle obj is the 'pen' that draw lines. 
my_screen = Screen() # screen obj is the 'sheet' or canvas. Its the window.

my_pen.screen.title("Turtle Graphics (Customized)") 
my_pen.speed(5) # Define the turtle's speed (1 to 10)

for _ in range(6):
    my_pen.forward(200)
    my_pen.left(60)

for _ in range(4):
    my_pen.forward(100)
    my_pen.right(90)

# Close the window on click
my_screen.exitonclick()
