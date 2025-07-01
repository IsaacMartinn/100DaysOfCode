from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0 
        self.penup()
        self.setposition(0,270)
        self.write(f'Score {self.score}',move=False,align="center",font=('Arial', 20, 'normal'))
        self.hideturtle()
        
    def increase_score(self):
        self.clear()
        self.write(f'Score {self.score}',move=False,align=ALIGNMENT,font=FONT)

    def game_over(self):
        self.setposition(0,0)
        self.write(f'GAME OVER',move=False,align="center",font=('Arial', 20, 'normal'))

        

        
