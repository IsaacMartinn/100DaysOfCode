# import colorgram

# colors = colorgram.extract('image.jpg', 30)
# # print(colors)
# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

from turtle import Turtle, Screen 
import random 
import turtle


tim = Turtle()
screen = Screen()
screen.setup(width=500, height=500,startx=0,starty=0)


color_list = [(200, 159, 94), (63, 88, 126), (138, 89, 51), (218, 205, 121), (135, 171, 194), (145, 54, 83), (123, 36, 48), (47, 54, 101), (139, 184, 144), (76, 25, 44), (174, 100, 109), (41, 41, 60), (150, 170, 66), (178, 144, 174), (94, 128, 179), (57, 40, 33), (182, 87, 77), (104, 155, 97), (169, 205, 154), (79, 73, 46), (76, 118, 116), (51, 71, 74), (212, 180, 189), (180, 188, 209), (215, 181, 173), (170, 199, 209)]

x_cor = -230
y_cor = -230
tim.penup()
tim.teleport(x_cor,y_cor)
turtle.colormode(255)

tim.speed("fastest")

for i in range(100):
    tim.color(random.choice(color_list))
    tim.dot(20)
    tim.forward(50)
    current_x_cor = tim.xcor()
    print(current_x_cor)
    if current_x_cor >= 230:
        y_cor += 50
        tim.teleport(x_cor,y_cor)


    





screen.exitonclick()