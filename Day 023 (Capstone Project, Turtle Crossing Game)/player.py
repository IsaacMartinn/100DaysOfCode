from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.teleport(STARTING_POSITION[0],STARTING_POSITION[1])
    
    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(),new_y)
    
    def restart(self):
        self.teleport(STARTING_POSITION[0],STARTING_POSITION[1])

