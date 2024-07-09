from turtle import Turtle 

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.seth(90)
        self.goto(STARTING_POSITION)
        
    # Create the movement of the Player object
    def move(self):
        self.forward(MOVE_DISTANCE)
    
    # Restart to the initial position of the Player object
    def level_up(self):
        self.goto(STARTING_POSITION)