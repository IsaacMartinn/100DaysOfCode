from turtle import Turtle, Screen
import random
import turtle

tim = Turtle()
screen = Screen()
turtle.colormode(255)

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color =  (r,g,b)
    return random_color


direction = [0, 90, 180, 270]

tim.speed("fastest")
tim.pensize(15)


for _ in range(200):
    tim.color(random_colour())
    tim.forward(30)
    tim.setheading(random.choice(direction))


screen.exitonclick()

# my_tuple = (1,3,8) #IMMUTABLE

# changed_tuple = list(my_tuple)

# #0-255