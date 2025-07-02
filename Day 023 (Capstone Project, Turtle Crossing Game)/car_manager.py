from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.penup()
        self.car_speed = STARTING_MOVE_DISTANCE

        self.teleport(x=300 ,y=random.randint(-250,250))
    
    def move_forward(self):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE
        self.goto(x=new_x,y=self.ycor())
    


    

    

    

    
        
    




