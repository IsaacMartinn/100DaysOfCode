from turtle import Turtle, Screen
import random

colors = [
    "red", "green", "blue", "yellow", "cyan", "magenta", "black", "gray",
    "orange", "purple", "pink", "brown", "lime", "indigo", "violet", "turquoise",
    "navy", "maroon", "teal", "olive", "coral", "salmon"
]


tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.color("blue")

num_of_sides = 3
drawing = True


while num_of_sides <= 10:
    angle = 360 / num_of_sides
    start_pos = tim.pos()

    for _ in range(num_of_sides):
        tim.forward(100)
        tim.right(angle)
    
    if tim.distance(start_pos) < 0.1:
        print(f"Back to start from {num_of_sides}")
    else:
        print("not back at start")
    
    num_of_sides += 1
    tim.color(random.choice(colors))

    









screen.exitonclick()