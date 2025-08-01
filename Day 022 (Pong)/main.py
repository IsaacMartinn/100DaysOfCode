from turtle import Screen
from paddle import Paddle
from ball import Ball
import time 
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.listen()
screen.onkey(fun=r_paddle.up,key="Up")
screen.onkey(fun=r_paddle.down,key="Down")
screen.onkey(fun=l_paddle.up,key="w")
screen.onkey(fun=l_paddle.down,key="s")

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on: 
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with the ball 
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) <50 and ball.xcor() <-320:
        ball.bounce_x()
        
    
    #Detect R paddle misses
    if ball.xcor() > 380: 
        ball.reset_position()
        scoreboard.l_point()

    #Detect if L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()





screen.exitonclick()