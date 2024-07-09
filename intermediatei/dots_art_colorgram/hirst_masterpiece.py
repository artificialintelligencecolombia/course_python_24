# Paint a hirst dotted art. Its a 10 x 10 squared matrix with dots with 20 of size and spacing of 50. Employ the color palette from main.py

# Import libraries
from turtle import Turtle, Screen
from color_extractor import rgb_colors
import random

# Create the objects
my_pen = Turtle() # turtle obj is the 'pen' that draw lines. 
my_screen = Screen() # screen obj is the 'sheet' or canvas. Its the window.
my_screen.colormode(255) # Color mode
my_pen.speed(0)



def draw_dots(columns, rows):
    # Set the initial position of the turtle object
    x_pos = -281
    y_pos = -281
    my_pen.penup()
    my_pen.setposition(x_pos, y_pos) # Define the initial position for center the dots art
    
    for _ in range(rows):
        
        for _ in range(columns):    
            # Color selection
            pen_color = random.choice(rgb_colors)
            my_pen.pencolor(pen_color)
            
            # Draw the dot
            my_pen.dot(20)
            my_pen.penup()
            my_pen.forward(50)
            my_pen.pendown()
        
        # Jump over the next line
        my_pen.penup()
        y_pos += 50
        my_pen.setposition(x_pos, y_pos)
        


draw_dots(12, 12)

# Close the window on click
my_screen.exitonclick()