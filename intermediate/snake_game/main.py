# Turtle is a python library for drawing shapes and patterns
from turtle import Turtle, Screen
import time
import random

# Define the screen settings
my_screen = Screen() # screen obj is the 'sheet' or canvas. Its the window.
my_screen.setup(width=600, height=600) # Setting the screen dimensions
my_screen.bgcolor("black")
my_screen.title("My snake game")
my_screen.tracer(0) # Disables automatic screen updates. Give us manual control

# Define the initial position of the turtles, in column coordinates
init_positions_xaxis = [0, -20, -40] # Initial positions for the snake segments
snake_body = []  # Create a list that composes the body of the snake in form of segments (turtle objects).

# Create the initial snake body with 3 segments
for i in range(0, 3):  # Three turtle objects
    new_turtle = Turtle()
    new_turtle.shape("square") 
    new_turtle.color("white") # Those are all the turtle's settings.
    new_turtle.penup() # Prevent the turtle from drawing when moving
    new_turtle.setposition(init_positions_xaxis[i], 0)
    snake_body.append(new_turtle)   

# Create the token for the snake movement
game_is_on = True

directions = [0, 90, 180, 270]
key_list = ['a','w','s','d','c']

# Main game loop
while game_is_on: 
    init_speed = 1
    my_screen.update() # Update the screen manually
    time.sleep(0.1) # Pause the execution for 0.1 seconds to control the game speed
    my_screen.listen()
    
    
    for segment in range(len(snake_body)-1, 0, -1):
        new_x = snake_body[segment-1].xcor()
        new_y = snake_body[segment-1].ycor()
        snake_body[segment].goto(new_x,new_y)

    snake_body[0].forward(20)
    snake_body[0].right(90)    
# Close the window on click
my_screen.exitonclick()