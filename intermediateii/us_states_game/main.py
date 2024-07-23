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

guessed_states = []
tkn = 0 # counter for correct guess

# Create a turtle for writing state names
writer = Turtle()
writer.penup()
writer.hideturtle()

def guess_state():
    global tkn # Bring the global variable into the function
    # -> USR INPUTS THE STATE NAME AND LIST FOR TRACKING THE GUESSED STATES
    usr_input = screen.textinput(title=f'{len(guessed_states)}/50 States correct', prompt='Input a state name: ').title()
    if usr_input in df.state.values:
        guessed_states.append(usr_input)
        state_data = df[df.state.values == usr_input] # state_data is a pandas dataframe with 1 record
        x, y = int(state_data.x), int(state_data.y)
        writer.goto(x, y)
        writer.write(state_data.state.values, font=("Arial",12))
        
        tkn += 1 # modify the global variable
        
    if len(guessed_states) == 50:
        turtle.bye()

while len(guessed_states) < 50:
    guess_state()

screen.exitonclick()