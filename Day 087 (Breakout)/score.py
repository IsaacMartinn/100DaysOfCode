from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 80, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.score = 0
        self.penup()
        self.hideturtle()
        self.teleport(0, 200)

    def score_point(self):
        self.clear()
        self.write(f"{self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)
