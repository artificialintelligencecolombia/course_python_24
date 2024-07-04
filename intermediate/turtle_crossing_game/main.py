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
        if player.distance(car) < 20:  # INCOMPLETE!! Adjust the distance threshold as needed
            print("Collision detected!")
            game_is_on = False
            break # Check if necessary
    
    #if player.ycor() > 250:
    #    player.level_up()
    #    for car in cars:
     #       car.increase_speed()
    
    loop_counter += 1
    
screen.exitonclick()