import turtle
import pandas

ALIGNMENT = "center"
FONT = ('Arial', 12, 'normal')

score = 0

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image) #add the image to the available shapes 
turtle.shape(image)

game_on = True

#getting the x and y coor. for each area on the map 
# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()

all_turtles = []
guessed_states = []

while game_on: 
    answer_state = screen.textinput(title=f'{score}/50 Guess the State', prompt = "What's another state's name? ").title()
    print(answer_state)

    if answer_state == "Exit":
        break

    for i in state_list:
        if i == answer_state:
            guessed_states.append(answer_state)
            row = data[data.state == answer_state]
            tim = turtle.Turtle()
            tim.hideturtle()
            tim.penup()
            x_coor = int(row.x.iloc[0])
            y_coor = int(row.y.iloc[0])
            tim.teleport(x_coor,y_coor)
            tim.write(answer_state, move=True,align=ALIGNMENT,font=FONT)
            
            all_turtles.append(tim)
            score += 1
            if score == 50:
                game_on = False

print(guessed_states)
missing_states = []
for state in state_list:
    if state not in guessed_states:
        missing_states.append(state)

new_data = pandas.DataFrame(missing_states)
new_data.to_csv("states_to_learn.csv")
