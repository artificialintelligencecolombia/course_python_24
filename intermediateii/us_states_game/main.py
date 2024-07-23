# -> IMPORT LIBRARIES
from turtle import Turtle, Screen
import pandas as pd

# -> LOAD THE CSV FILE
FILEPATH = './50_states.csv'
IMGPATH = './blank_states_img.gif'
df = pd.read_csv(FILEPATH)

# -> SET UP THE SCREEN AND THE TURTLE IMG OBJECT
screen = Screen() # Create the screen obj
turtle = Turtle() # Create the turtle obj that will be used to display the image
screen.title("US States Game")
screen.addshape(IMGPATH) # Add the image shape to the screen, making it available for the turtle object to use
turtle.shape(IMGPATH) # Set the shape of the turtle object to the custom image shape

# -> USR INPUTS THE STATE NAME
usr_input = screen.textinput(title='Guess a state', prompt='Input a state name: ')
if usr_input.title() in df['state'].values:
    state_turtle = Turtle()
    state_turtle.penup()
    state_turtle.goto(10,100)
    state_turtle.write(usr_input.title())

screen.exitonclick()