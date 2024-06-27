#!usr/bin/env python3

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

# Create the objects
player = Player()
car = CarManager() 

# Enable key event listening and binding arrow keys to the snake's move_ methods
screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
loop_counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car.move_car()
    
    loop_counter += 1
    print(loop_counter)
    
screen.exitonclick()