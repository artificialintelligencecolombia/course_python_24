from turtle import Turtle, Screen

turtle = Turtle()

for _ in range(5):
    for _ in range(10):
        turtle.color("green")
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()
    turtle.left(72)
    
screen = Screen()
screen.exitonclick()