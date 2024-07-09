# Turtle is a python library for drawing shapes and patterns
from turtle import Turtle, Screen


# Create the objects
my_pen = Turtle() # turtle obj is the 'pen' that draw lines. 
my_screen = Screen() # screen obj is the 'sheet' or canvas. Its the window.
my_pen.speed(1)

directions = [0, 90, 180, 270]
key_list = ['a','w','s','d','c']


# Create a function that will be activated by the even listener
def move_right():
    my_pen.setheading(directions[0])
    my_pen.forward(20)
    
def move_left():
    my_pen.setheading(directions[2])
    my_pen.forward(20)

def move_up():
    my_pen.setheading(directions[1])
    my_pen.forward(20)

def move_down():
    my_pen.setheading(directions[3])
    my_pen.forward(20)

def clear():
    my_pen.clear()

my_screen.listen() # Set focus on screen object in order to collect key-events.

my_screen.onkey(fun=move_right,key=key_list[3]) 
my_screen.onkey(fun=move_left,key=key_list[0])
my_screen.onkey(fun=move_up,key=key_list[1])
my_screen.onkey(fun=move_down,key=key_list[2])
my_screen.onkey(fun=clear,key=key_list[4])

# Close the window on click
my_screen.exitonclick()
