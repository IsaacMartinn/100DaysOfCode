from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red","orange","yellow","green","blue","purple"]
all_turtles = []

y_cor = -100

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_cor)
    y_cor += 30
    all_turtles.append(new_turtle)

is_race_on = False
if  user_bet: 
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
        

        if turtle.xcor() >= 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            






screen.exitonclick()