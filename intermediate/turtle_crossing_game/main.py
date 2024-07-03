#!usr/bin/env python3

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

# Create the objects
player = Player()
cars = []

# Enable key event listening and binding arrow keys to the snake's move_ methods
screen.listen()
screen.onkey(player.move, "Up")

# Detect collision through the function
def is_collision(player_obj, car_obj):
    # Calculate the bounding box for the player
    player_x_min = player_obj.xcor() - 10  # Left edge of the player bounding box
    player_x_max = player.xcor() + 10  # Right edge of the player bounding box
    player_y_max = player_obj.ycor() + 10  # Top edge of the player bounding box
    player_y_min = player_obj.ycor() - 10  # Bottom edge of the player bounding box
    
    # Calculate the bounding box for the car
    car_x_min = car_obj.xcor() - 20  # Left edge of the car bounding box
    car_x_max = car_obj.xcor() + 20  # Right edge of the car bounding box
    car_y_max = car_obj.ycor() + 10  # Top edge of the car bounding box
    car_y_min = car_obj.ycor() - 10  # Bottom edge of the car bounding box

game_is_on = True
loop_counter = 0

while game_is_on:
    # Update the screen and pause
    time.sleep(0.1)
    screen.update()
    
    # Increment the loop counter for creating new car only every 6th time the game loop runs
    if loop_counter % 6 == 0:
        car = CarManager()
        cars.append(car)
    
    # Manage the cars    
    for car in cars:
        car.drive()
          
        # Detect collision between turtle and cars
        if player.distance(car) < 22:  # Adjust the distance threshold as needed
            print("Collision detected!")
            game_is_on = False
            break # Check if necessary
    
    loop_counter += 1
    
screen.exitonclick()