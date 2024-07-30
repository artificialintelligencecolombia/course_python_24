# -> IMPORT LIBRARIES
from turtle import Turtle, Screen
import pandas as pd

# -> LOAD THE CSV FILE
FILEPATH = './50_states.csv'
IMGPATH = './blank_states_img.gif'
df = pd.read_csv(FILEPATH)

# -> SET UP THE SCREEN AND THE TURTLE IMG OBJECT
screen = Screen() # Create the screen object
turtle = Turtle() # Create the turtle object for displaying the image
screen.title("US States Game")
screen.addshape(IMGPATH) # Add the image shape to the screen, making it available for the turtle object to use
turtle.shape(IMGPATH) # Set the shape of the turtle object to the custom image

guessed_states = [] # List to keep track of guessed states
missing_states = []
tkn = 0 # counter for correct guess


# Create a turtle for writing state names
writer = Turtle()
writer.penup()
writer.hideturtle()

def guess_state():
    # -> USR INPUTS THE STATE NAME AND LIST FOR TRACKING THE GUESSED STATES
    usr_input = screen.textinput(title=f'{len(guessed_states)}/50 States correct', prompt='Input a state name: ')
    if usr_input:    
        usr_input = usr_input.title() # Capitalize the user input
        
        if usr_input == 'Exit':
            missing_states = [state for state in df.state.values if state not in guessed_states]
            # For each state in df.state.values that is not found in guessed_states, the state name is included in the new list missing_states.
            with open('./missing_states.csv', 'w') as f:
                for state in missing_states:
                    f.write(f'{state}\n')
            return False # Return False to exit the game loop
            
        if usr_input in df.state.values:
            guessed_states.append(usr_input) # Add correct guess to the list
            state_data = df[df.state.values == usr_input].iloc[0] # Retrieve state data
            x, y = int(state_data['x'].iloc[0]), int(state_data['y'].iloc[0]) # Get coordinates
            writer.goto(x, y)
            writer.write(usr_input, font=("Arial",12))
            
        if len(guessed_states) == 50:
            return False # Exit the game loop if all states are guessed
    else:
        return False  # Exit the game loop if no inputturtle.bye() # condition of ending the game if the user didn't input anything
    return True    
while len(guessed_states) < 50:
    guess_state() # Loop continues as long as guess_state() returns True

screen.bye()  # Close the screen when the game ends