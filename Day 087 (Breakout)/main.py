from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
from block import Block
import time

screen = Screen()
ball = Ball()
scoreboard = Score()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("BreakOut")

# screen.tracer(0)

paddle = Paddle()
scoreboard.score_point()

start_x = 350
end_x = -420
step = -85
y_coordinate = 0
blocks = []

while y_coordinate <= 125:
    for x in range(start_x, end_x, step):
        block = Block(x, y_coordinate)
        blocks.append(block)
        if x == -415:
            y_coordinate += 25

screen.listen()
screen.onkey(key='Left', fun=paddle.go_left)
screen.onkey(key='Right', fun=paddle.go_right)

game_is_on = True
while game_is_on:

    time.sleep(0.05)
    ball.move_1()
    screen.update()

    #detect collision paddle
    if ball.distance(paddle) < 30 and ball.ycor() > -305:
        ball.bounce_y()

    #detect collision with wall
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    #detect collection with top wall on y-axis
    if ball.ycor() > 280:
        ball.bounce_y()

    #detection of block
    for block in blocks:
        if ball.distance(block) < 30:
            ball.bounce_y()
            block.hideturtle()
            blocks.remove(block)

            scoreboard.score += 1
            scoreboard.score_point()
            screen.update()

    if len(blocks) == 0:
        scoreboard.game_over()

screen.exitonclick()
