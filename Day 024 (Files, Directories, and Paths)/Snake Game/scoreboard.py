from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0 
        self.high_score = 0
        self.penup()
        self.setposition(0,270)
        self.write(f'Score {self.score}',move=False,align="center",font=('Arial', 20, 'normal'))
        self.hideturtle()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score} ',move=False,align=ALIGNMENT,font=FONT)
    
    def reset(self):
        if self.score > self.high_score: 
            self.high_score = self.score
        self.score = 0 
        self.increase_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.setposition(0,0)
    #     self.write(f'GAME OVER',move=False,align="center",font=('Arial', 20, 'normal'))

        

        
