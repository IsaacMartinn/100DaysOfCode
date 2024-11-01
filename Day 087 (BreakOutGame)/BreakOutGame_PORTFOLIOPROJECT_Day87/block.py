from turtle import Turtle
import random

COLOR_LIST = ['light blue', 'royal blue',
              'light steel blue', 'steel blue',
              'light cyan', 'light sky blue',
              'violet', 'salmon', 'tomato',
              'sandy brown', 'purple', 'deep pink',
              'medium sea green', 'khaki']


class Block(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.color(random.choice(COLOR_LIST))
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.teleport(x_cor, y_cor)




