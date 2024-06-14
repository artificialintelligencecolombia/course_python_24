# Turtle is a python library for drawing shapes and patterns
from turtle import Turtle, Screen
from snake import Snake 
from food import Food 
from scoreboard import Scoreboard
import time
import random

# Define the screen settings
my_screen = Screen() # screen obj is the 'sheet' or canvas. Its the window.
my_screen.setup(width=600, height=600) # Setting the screen dimensions
my_screen.bgcolor("black")
my_screen.title("My snake game")
my_screen.tracer(0) # Disables automatic screen updates. Give us manual control

# Create the snake, food and score
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Enable key event listening and binding arrow keys to the snake's move_ methods
my_screen.listen()
my_screen.onkey(snake.move_up, "Up")
my_screen.onkey(snake.move_down, "Down") 
my_screen.onkey(snake.move_left, "Left") 
my_screen.onkey(snake.move_right, "Right") 

# Create the token for the snake movement
game_is_on = True
# Main game loop
while game_is_on: 
    init_speed = 1
    my_screen.update() # Update the screen manually
    time.sleep(0.1) # Pause the execution for 0.1 seconds to control the game speed
    snake.move() # Move the snake
    
    # Detect when snake collisions with food
    if snake.snake_body[0].distance(food) < 15: 
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
        
    # Detect when snake collisions with wall
    if snake.snake_body[0].xcor() > 280 or snake.snake_body[0].xcor() < -280 or snake.snake_body[0].ycor() > 280 or snake.snake_body[0].ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
        
    # Detect when snake collisions with tail
    for segment in snake.snake_body[1:]:
        if snake.snake_body[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
     
# Close the window on click
my_screen.exitonclick()