#cirlc radius of 100 
from turtle import Turtle, Screen
import random
import turtle


tim = Turtle()
screen = Screen()
turtle.colormode(255)

tim.speed("fastest")


def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color =  (r,g,b)
    return color


angle = 0 

while angle <= 360:
    tim.color(random_colour())
    tim.circle(100)
    tim.setheading(angle)
    angle += 5



screen.exitonclick()