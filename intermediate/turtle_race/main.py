# Create a game that consists in a turtle's race. The user has to guess which will be the winner turtle by calling it by it s color.

# Turtle is a python library for drawing shapes and patterns
from turtle import Turtle, Screen
import random

# Create the turtles objects list
winner_turtle = ""
is_race_on = True
turtles_list = [] # List of turtle objects
turtle_colors = ["yellow", "orange","red", "purple", "blue", "green"] # List of turtle colors

# Define the screen measurements for the race and finish conditions
my_screen = Screen() # screen obj is the 'sheet' or canvas. Its the window.
my_screen.setup(width=1200, height=600) # Setting the screen dimensions

# Define the initial position of the turtles, in column coordinates
init_positions_yaxis = [90, 60, 30, 0, -30, -60]

# Create the objects
for i in range(0, 6): # Six turtle objects
    new_turtle = Turtle()
    new_turtle.shape("turtle") 
    new_turtle.color(turtle_colors[i]) # Those are all the turtle's settings.
    new_turtle.penup()
    new_turtle.setposition((-580 ,init_positions_yaxis[i]))
    turtles_list.append(new_turtle)
    new_turtle.pendown()

user_bet = my_screen.textinput(title="Make your bet:", prompt="Which turtle will win the race? Enter a color: ")

# Token activator
if user_bet: 
    is_race_on = True

# While the race is on, iterate over each turtle, moving them at random speed intervals.    
while is_race_on:
    
    # Define a random speed in each loop iteration for each turtle.
    for turtle in turtles_list:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

    # Condition for stop the race
    for turtle in turtles_list:
        if turtle.xcor() > 600:
            is_race_on = False
            winner_turtle = turtle.color()[0] # .color() has (fill_color, line_color), thats why we call [0]
            break

# Compare the user bet against the winner. Print the results
if winner_turtle == user_bet:
    print(f"Your guess is correct. WINNER: {winner_turtle}")
else:
    print(f"You lose the bet. WINNER: {winner_turtle}")
    
# Close the window on click
my_screen.exitonclick()
