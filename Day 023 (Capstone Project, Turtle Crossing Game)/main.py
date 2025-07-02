import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from player import FINISH_LINE_Y

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()


screen.listen()
screen.onkey(fun=player.up,key="Up")

all_cars = []
i = 0

scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    i += 1 
    if i % 6 == 0:
        new_car = CarManager()
        all_cars.append(new_car)
    for car in all_cars:
        car.move_forward()

        #Detect when the turtle collides with car
        if player.distance(car) < 30:
            game_is_on = False
            scoreboard.game_over()

    #Detect when turtle has crossed finish line
    if player.ycor() > FINISH_LINE_Y:
        player.restart()
        scoreboard.increase_score()
        #NEED to place a way to increase speed


    
screen.exitonclick()